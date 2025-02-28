import unittest
from src.shoppingCart import ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        print("* setUp")
        self.shoppingCart = ShoppingCart()

    def test_add_product(self):
        print("** test_add_product")
        self.shoppingCart.add_product("Apple", 2, 5)
        self.shoppingCart.add_product("Apple", 3, 6)
        self.assertIn("Apple", self.shoppingCart.products)
        self.assertEqual(self.shoppingCart.products["Apple"]["quantity"], 5)
        self.assertEqual(self.shoppingCart.products["Apple"]["price"], 2)

    def test_remove_product(self):
        print("** test_remove_product")
        self.shoppingCart.remove_product("Apple")
        self.assertNotIn("Apple", self.shoppingCart.products)

    def test_update_quantity(self):
        print("** test_update_quantity")
        self.shoppingCart.add_product("Apple", 2, 5)
        self.shoppingCart.update_quantity("Apple", 2)
        self.assertEqual(self.shoppingCart.products["Apple"]["quantity"], 2)
        self.shoppingCart.update_quantity("Apple", 0)
        self.assertNotIn("Apple", self.shoppingCart.products)

    def test_get_products(self):
        print("** test_get_prod")
        self.shoppingCart.add_product("Apple", 2, 5)
        self.assertEqual(self.shoppingCart.get_products(), ["Apple"])

    def test_count_products(self):
        print("** test_count_prod")
        self.shoppingCart.add_product("Apple", 2, 5)
        self.shoppingCart.add_product("Banana", 1, 3)
        self.assertEqual(self.shoppingCart.count_products(), 8)

    def test_get_total_price(self):
        print("** test_get_total_price")
        self.shoppingCart.add_product("Apple", 2, 5)
        self.shoppingCart.add_product("Banana", 1, 3)
        self.assertEqual(self.shoppingCart.get_total_price(), 13)

    def test_apply_discount_code(self):
        print("** test_apply_discount")
        self.shoppingCart.add_product("Apple", 10, 2)
        self.assertTrue(self.shoppingCart.apply_discount_code("DISCOUNT10"))
        self.assertEqual(self.shoppingCart.products["Apple"]["price"], 9)
        self.assertFalse(self.shoppingCart.apply_discount_code("INVALID"))

    def test_checkout(self):
        print("** test_checkout")
        self.shoppingCart.add_product("Apple", 2, 5)
        self.assertTrue(self.shoppingCart.checkout())
        self.assertEqual(self.shoppingCart.products, {})
        self.assertFalse(self.shoppingCart.checkout())

    def tearDown(self):
        self.shoppingCart = None

    if __name__ == '__main__':
        unittest.main()
