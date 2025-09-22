from typing import Optional, List, Dict
from src.config import get_supabase

class OrderDAO:
    def _sb(self):
        return get_supabase()
    
    def get_order_by_cust_id(self, cust_id: str) -> Optional[Dict]:
        pass