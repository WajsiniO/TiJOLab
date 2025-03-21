from Order import Order
from OrderValidator import OrderValidator
from OrderCommunicator import OrderCommunicator

class OrderProcessor:
    def __init__(self, order):
        self.order = order

    def process_order(self):
        OrderValidator._validate_order(self.order)
        OrderCommunicator._save_order_to_database(self.order)
        OrderCommunicator._send_confirmation_email(self.order)






