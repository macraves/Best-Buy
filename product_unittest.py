"""products.py test Interface"""
import unittest
from products import Product, ClassMethodException


class TestProduct(unittest.TestCase):
    """Check what is TestCase"""

    def setUp(self):  # Some How setUp not need a doc string
        self.product = Product("Test Product", 10.0, 100)

    def test_name(self):
        """Test valid name"""
        self.assertEqual(self.product.name, "Test Product")

        # Test invalid name (non-string)
        with self.assertRaises(ClassMethodException):
            self.product.name = 123

    def test_quantity(self):
        """Test valid quantity"""
        self.assertEqual(self.product.quantity, 100)

        # Test invalid quantity (non-integer)
        with self.assertRaises(ClassMethodException):
            self.product.quantity = 3.14

        # Test invalid quantity (negative)
        with self.assertRaises(ClassMethodException):
            self.product.quantity = -10

    def test_set_quantity(self):
        """Test valid set_quantity"""
        self.product.set_quantity(50)
        self.assertEqual(self.product.quantity, 150)

        # Test invalid set_quantity (exceeding max stock entry)
        with self.assertRaises(ClassMethodException):
            self.product.set_quantity(2001)

    def test_is_active(self):
        """Test is active?? Bu ne ChatGpt"""
        self.assertTrue(self.product.is_active())

        with self.assertRaises(ClassMethodException):
            self.product.set_quantity(0)

    def test_buy(self):
        """Test valid buy"""
        total_price = self.product.buy(50)
        self.assertEqual(total_price, 500.0)
        self.assertEqual(self.product.quantity, 50)

        # Test buy with a quantity larger than available
        with self.assertRaises(ClassMethodException):
            self.product.buy(200)

        # Test buy with an invalid buyer request
        with self.assertRaises(ClassMethodException):
            self.product.buy(700)


if __name__ == '__main__':
    unittest.main()
