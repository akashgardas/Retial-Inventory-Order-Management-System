from typing import Optional, List, Dict
from src.config import get_supabase

class OrderDAO:
    TABLE = 'orders'
    
    def _sb(self):
        return get_supabase()
    
    def add_order(self, cust_id: int, total_amount: float, status: str = 'PLACED') -> Optional[Dict]:
        order = {
            'cust_id': cust_id,
            'total_amount': total_amount,
            'status': status
        }
        resp = self._sb().table(self.TABLE).insert(order).execute()
        return resp.data[0] if resp.data else None
    
    def get_order_by_cust_id(self, cust_id: str) -> Optional[Dict]:
        resp = self._sb().table(self.TABLE).select('*').eq('cust_id', cust_id).execute()
        return resp.data[0] if resp.data else None
    
    def get_order_by_order_id(self, order_id: int) -> Optional[Dict]:
        resp = self._sb().table(self.TABLE).select('*').eq('cust_id', order_id).execute()
        return resp.data[0] if resp.data else None
    
    def update_dao(self, order_id, fields: Dict) -> Optional[Dict]:
        self._sb().table(self.TABLE).update(fields).execute()
        resp = self.get_order_by_order_id(order_id)
        return resp.data[0] if resp.data else None
    
    