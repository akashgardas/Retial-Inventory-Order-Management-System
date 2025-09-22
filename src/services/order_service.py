from typing import List, Dict
from src.dao.order_dao import OrderDAO
from src.dao.customer_dao import CustomerDAO
from src.dao.product_dao import ProductDAO
from src.dao.order_items_dao import OrderItemsDao
from src.dao.payment_dao import PaymentDAO

class OrderError(Exception):
    pass

class OrderService:
    def __init__(self):
        self.order_dao = OrderDAO()
        self.customer_dao = CustomerDAO()
        self.product_dao = ProductDAO()
        self.order_items_dao = OrderItemsDao()
        self.payment_dao = PaymentDAO()
    
    def create_order(self, cust_id: str, items: List):
        '''
        Validates Customer and places order
        '''
        
        # Validate customer
        customer_exists = self.customer_dao.get_customer_by_cust_id(cust_id)
        
        if not customer_exists:
            raise OrderError('Customer doesn\'t exists')
        
        total_amount = 0
        
        # Validate product stock
        for item in items:
            prod_id = item.prod_id
            quantity = item.quantity
            prod_existing = self.product_dao.get_product_by_id(prod_id)

            if not prod_existing:
                raise OrderError(f"{item} doesn't exists")
            
            stock = prod_existing.stock
            if stock < quantity:
                raise OrderError(f'Stock is not available. Available Stock: {stock}, Requested quantity: {quantity}')
            
            total_amount += prod_existing.price
        
        # adding order
        order = self.order_dao.add_order(cust_id, total_amount)
        
        # deducting the quantify from stock in the db
        for item in items:
            prod_id = item.prod_id
            quantity = item.quantity
            
            item_price = self.product_dao.get_product_by_id(prod_id).price
            self.product_dao.update_product(prod_id, {'stock': stock - quantity})

            # adding items ordered
            self.order_items_dao.add_order_item(order.order_id, prod_id, quantity, item_price)
        
        # adding payment
        self.payment_dao.create_payment(order.order_id, total_amount)
    
    def get_order_details(self, order_id: int) -> List:
        order = self.order_dao.get_order_by_order_id(order_id)
        customer = self.customer_dao.get_customer_by_cust_id(order.cust_id)
        order_items = self.order_items_dao.get_order_items_by_order_id(order_id)
        
        return [order, customer, order_items]
    
    def get_order_details_by_customer(self, cust_id: int) -> Dict:
        return self.order_dao.get_order_by_cust_id(cust_id)
    
    def cancel_order(self, order_id: int) -> Dict:
        order_exists = self.order_dao.get_order_by_order_id(order_id)
        if not order_exists:
            raise OrderError("Order doesn't exists")
        
        if order_exists.status == 'PLACED':
            # restock items
            order_item = self.order_items_dao.get_order_items_by_order_id(order_id)
            prod_stock = self.product_dao.get_product_by_id(order_item.prod_id).stock
            restock_quantity = order_item.quantity
            updated_product = self.product_dao.update_product(order_item.prod_id, {'stock': prod_stock + restock_quantity})
            
            # delete order_item from order_items
            deleted_order_item = self.order_items_dao.delete_order_items(order_id)
            
            # update customer order status
            updated_order = self.order_dao.update_order(order_id, {'status': 'CANCELLED'})
            
            # refund amount
            payment_refund = self.payment_dao.refund_payment(order_id, status='REFUNDED')
        
            return [updated_order, updated_product, deleted_order_item, payment_refund]
        
        return {}
    