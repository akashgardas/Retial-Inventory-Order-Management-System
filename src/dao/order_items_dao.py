from typing import Optional, List, Dict
from src.config import get_supabase

class OrderItemsDao:
    TABLE = 'order_items'
    
    def _sb(self):
        return get_supabase()
    
    def add_order_item(self, order_id: int, prod_id: int, quantity: int, price: float) -> Optional[Dict]:
        item = {
            'order_id': order_id,
            'prod_id': prod_id,
            'quantity': quantity,
            'price': price
        }
        resp = self._sb().table(self.TABLE).insert(item).execute()
        return resp.data[0] if resp.data else None
    
    def get_order_items_by_order_id(self, order_id: int) -> Optional[Dict]:
        resp = self._sb().table(self.TABLE).select('*').eq('order_id', order_id).execute()
        return resp.data[0] if resp.data else None
    
    def delete_order_item(self, order_id: int) -> Optional[Dict]:
        resp = self.get_order_items_by_order_id(order_id)
        self._sb().table(self.TABLE).delete().eq('order_id', order_id).execute()
        
        return resp.data[0] if resp.data else None
    
    