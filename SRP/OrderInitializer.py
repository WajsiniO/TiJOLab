from Order import Order
from OrderProccesor import OrderProcessor

class OrderInitializer:
    def __init__(self):
        self.order = Order("123", ["Produkt A", "Produkt B"], "Jan Kowalski")
        self.processor = OrderProcessor(self.order)


    def startUp(self):
        self.processor.process_order()

orderInitializer = OrderInitializer()
orderInitializer.startUp()