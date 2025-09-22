from typing import List, Dict
from src.dao.customer_dao import CustomerDAO
from src.dao.order_dao import OrderDAO

class CustomerError(Exception):
    pass


class CustomerService:
    def __init__(self):
        self.customer_dao = CustomerDAO()
        self.order_dao = OrderDAO()
        
    def add_customer(self, name: str, email: str, phone: str, city: str | None = None) -> Dict:
        '''
        Validates email and adds a new customer.
        Raises CustomerError on validation failure
        '''
        
        if not phone.isdigit() or len(phone) != 10:
            raise CustomerError('Phone must be a 10 digit number')
        
        if name.strip() == '':
            raise CustomerError('Name should not be empty')
        
        if email.strip() == '' or '@' not in email:
            raise CustomerError('Invalid Email')

        existing = self.customer_dao.get_customer_by_email(email)
        
        if existing:
            raise CustomerError(f'Email already exists: {email}')
        
        return self.customer_dao.create_customer(name, email, phone, city)
    
    def update_customer(self, cust_id: int, phone: str | None = None, city: str | None = None) -> Dict:
        '''
        Validates the new detail and updates.
        Returns the updated row.
        Raises error if both phone and city are empty or if phone and city formats are not appropriate.
        '''
        
        new_details = {}
        if phone:
            if not phone.isdigit() or len(phone) != 10:
                raise CustomerError('Phone must be a 10 digit number')
            
            new_details['phone'] = phone
            
        if city:
            if city.strip() == '':
                raise CustomerError('City cannot be empty')
            
            new_details['city'] = city
        
        if not phone and not city:
            raise CustomerError('Phone must not be empty')
        
        return self.customer_dao.update_customer(cust_id, new_details)
    
    def delete_customer(self, cust_id: str) -> Dict:
        '''
        Validates Customer and deletes
        Raises Customer Error if customer has got orders
        '''
        
        existing_orders = self.order_dao.get_order_by_cust_id(cust_id)
        
        if existing_orders:
            raise CustomerError('Customer cannot be deleted with orders existing')
        
        return self.customer_dao.delete_customer(cust_id)
     
    def search_customer(self, email: str | None = None, city: str | None = None) -> Dict:
        '''
        Searches customers based on email and/or city
        Returns the search records
        Raise Customer Error if validation fails
        '''
        
        if email:
            if email.strip() == '' or '@' not in email:
                raise CustomerError('Invalid Email')
            
            return self.customer_dao.get_customer_by_email(email)
        elif city:
            if city.strip() == '':
                raise CustomerError('City cannot be empty')
            
            return self.customer_dao.get_customer_by_city(city)
        
        if not email and not city:
            raise CustomerError('Either Email or City has to be specified') 