from typing import List, Dict
from src.dao.payment_dao import PaymentDAO

class PaymentError(Exception):
    pass


class PaymentServcie:
    
    def __init__(self):
        self.payment_dao = PaymentDAO()
        
    def process_payment(self, order_id: int) -> Dict:
        return self.payment_dao.complete_payment(order_id, 'COMPLETED')

