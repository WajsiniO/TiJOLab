class ShoppingCart:
    def __init__(self):
        self.products = {}
    def add_product(self, product_name: str, price: int, quantity: int) -> bool:
        """Dodawanie produktu do koszyka"""
        if product_name not in self.products:
            self.products[product_name] = {'price': price, 'quantity': quantity}
        return True


    def remove_product(self, product_name: str) -> bool:
        """Usuwanie produktu z koszyka"""
        if product_name in self.products:
            self.products.pop(product_name)
        return True

    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        """Aktualizacja ilości produktu w koszyku"""
        if product_name in self.products:
            if new_quantity > 0:
                self.products[product_name]['quantity'] = new_quantity
            else:
                self.remove_product(product_name)
        return True


    def get_products(self):
        """Pobieranie nazw produktów z koszyka"""
        return list(self.products.keys())

    def count_products(self) -> int:
        """Pobieranie liczby wszystkich produktów w koszyku"""
        return sum(product['quantity'] for product in self.products.values())

    def get_total_price(self) -> int:
        """Pobieranie sumy cen produktów w koszyku"""
        return sum(product['price'] * product['quantity'] for product in self.products.values())

    def apply_discount_code(self, discount_code: str) -> bool:
        """Zastosowanie kuponu rabatowego"""
        discounts = {
            "DISCOUNT10": 0.10,
            "DISCOUNT20": 0.20,
        }

        if discount_code in discounts:
            discount = discounts[discount_code]
            for product in self.products.values():
                product['price'] *= (1 - discount)
            return True
        return False

    def checkout(self) -> bool:
        """Realizacja zamówienia"""
        if not self.products:
            return False
        self.products.clear()
        return True


