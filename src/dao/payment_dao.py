from typing import Optional, List, Dict
from src.config import get_supabase

class PaymentDAO:
    TABLE = 'payments'
    
    def _sb(self):
        return get_supabase()
    
    def create_payment(self, order_id: int, amount: float, method: str = 'CASH', status: str = 'PENDING') -> Optional[Dict]:
        payment = {
            'order_id': order_id,
            'amount': amount,
            'method': method,
            'status': status
        }
        
        resp = self._sb().table(self.TABLE).insert(payment).execute()
        return resp.data[0] if resp.data else None
    
    def complete_payment(self, order_id, status: str) -> Optional[Dict]:
        self._sb().table(self.TABLE).update({'status': status}).eq('order_id', order_id).execute()
        resp = self._sb().table(self.TABLE).select('*').eq('order_id').execute()
        return resp.data[0] if resp.data else None
    
    def refund_payment(self, order_id, status: str) -> Optional[Dict]:
        self._sb().table(self.TABLE).update({'status': status}).eq('order_id', order_id).execute()
        resp = self._sb().table(self.TABLE).select('*').eq('order_id').execute()
        return resp.data[0] if resp.data else None
    
        