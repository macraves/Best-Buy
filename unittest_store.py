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

    # def test_remove_produck


if __name__ == "__main__":
    unittest.main()
