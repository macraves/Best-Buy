"""Unittest of store.py"""
import unittest
from store import Store, StoreExceptions as se
from products import Product


class Teststore(unittest.TestCase):
    """Unittest instance tests Store instance"""
    # assigning Store instance to Test instance

    def setUp(self) -> None:
        self.product1 = Product("Product1", 10, 50)
        self.product2 = Product("Product2", 20, 100)
        self.store = Store([self.product1, self.product2])

    def test_add_product(self):
        """Test to add new valid product to stock list"""
        third_product = Product("Product3", 30, 300)
        self.store.add_product(third_product)
        self.assertIn(third_product, self.store.stock)
        # Invalid object raises exception
        with self.assertRaises(se):
            self.store.add_product("New Product")

    def test_total_quantity_in_stock(self):
        """Product 1: 50
           Product 2: 100
           Total   :  150"""
        self.assertEqual(self.store.get_total_quantity(), 150)

    def test_active_products(self):
        """User can not deactivate Product unless it run out"""
        buy_whole = self.product1.buy(50)
        self.assertEqual(buy_whole, 500)
        # Product1 quantity 0 then:
        active_products = len(self.store.get_all_products())
        self.assertEqual(active_products, 1)

    def test_get_all_products(self):
        """setUp added only 2 Products"""
        self.assertEqual(len(self.store.get_all_products()), 2)

    def test_remove_product(self):
        """Testing remove_methods"""
        # Removing Invalid object raises exception
        with self.assertRaises(se):
            self.store.remove_product("None Product Type any object")
        # Product is not in list
            self.store.remove_product(Product("Product4", 100, 100))
        # Attempt remove from empty stock raises exception
        self.store.remove_product(self.product1)
        self.store.remove_product(self.product2)
        with self.assertRaises(se):
            self.store.remove_product(self.product1)


if __name__ == "__main__":
    unittest.main()
