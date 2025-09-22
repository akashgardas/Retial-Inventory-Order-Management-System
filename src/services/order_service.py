from typing import List, Dict
from src.dao.order_dao import OrderDAO
from src.dao.customer_dao import CustomerDAO

class OrderError(Exception):
    pass

class OrderService:
    def __init__(self):
        self.order_dao = OrderDAO()
        self.customer_dao = CustomerDAO()
    
    def create_order(self, cust_id: str, items: List):
        '''
        Validates Customer and places order
        '''
        
        # Validate customer
        customer_exists = self.customer_dao.get_customer_by_cust_id(cust_id)
        
        if not customer_exists:
            raise OrderError('Customer doesn\'t exists')
        
        # Validate product stock
        for item in items:
            prod_id = item.prod_id
            quantity = item.quantity
            
    
    def get_order_details(self):
        pass
    
    def cancel_order(self):
        pass