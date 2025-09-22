from typing import Optional, List, Dict
from src.config import get_supabase

class CustomerDAO:
    def _sb(self):
        return get_supabase()
    
    def create_customer(self, name: str, email:str , phone: str, city: str | None = None) -> Optional[Dict]:
        '''
        Insert a customer and return the inserted row.
        Insert and select by email
        '''
        
        payload = {
            'name': name, 
            'email': email, 
            'phone': phone
            }
        
        if not city:
            payload['city'] = city
        
        # Insert
        self._sb().table('customers').insert(payload).execute()
        
        # Fetch inserted row by email
        resp = self._sb().table('customers').select('*').eq('email', email).limit(1).execute()
        
        return resp.data[0] if resp.data else None
    
    def get_customer_by_email(self, email: str) -> Optional[Dict]:
        resp = self._sb().table('customers').select('*').eq('email', email).limit(1).execute()
        
        return resp.data[0] if resp.data else None
    
    def get_customer_by_city(self, email: str) -> Optional[Dict]:
        resp = self._sb().table('customers').select('*').eq('city', city).limit(10).execute()
        
        return resp.data[0] if resp.data else None
    
    def get_customer_by_cust_id(self, cust_id: int) -> Optional[Dict]:
        resp = self._sb().table('customers').select('*').eq('cust_id', cust_id).limit(1).execute()
        
        return resp.data[0] if resp.data else None
    
    def update_customer(self, cust_id: int, fields: Dict) -> Optional[Dict]:
        '''
        Updates and returns the updated row
        '''
        
        self._sb().table('customers').update(fields).eq('cust_id', cust_id).execute()
        
        resp = self._sb().table('customers').select('*').eq('cust_id', cust_id).limit(1).execute()
        
        return resp.data[0] if resp.data else None
    
    def delete_customer(self, cust_id: str) -> Optional[Dict]:
        resp = self._sb().table('customers').delete().eq('cust_id', cust_id).execute()
        
        return resp.data[0] if resp.data else None
    
    def list_customers(self, limit: int = 100) -> Optional[Dict]:
        resp = self._sb().table('customers').select('*')
        
        return resp.data[0] if resp.data else None
    
    