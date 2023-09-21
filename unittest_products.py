"""Test that creating a normal product works.
Test that creating a product with invalid details (empty name, negative price) invokes an exception.
Test that when a product reaches 0 quantity, it becomes inactive.
Test that product purchase modifies the quantity and returns the right output.
Test that buying a larger quantity than exists invokes exception"""

import unittest
from products import Product, ClassMethodException as clsex


class TestProducts(unittest.TestCase):
    """Creating unittest instance to check products methods"""

    def setUp(self) -> None:
        self.product1 = Product("test string", 10.0, 100)

    def validate_names(self):
        """Test that creating a product with 
        invalid details (empty name, negative price) 
        invokes an exception."""
        # valid entry check
        self.assertTrue(self.product1.name, "Test String")
        # empty string raises exception check
        with self.assertRaises(clsex):
            Product(" ", 10, 10)
        # none str entry invokes exception
            self.product1.name = 000

    def test_quantity(self):
        """User cannot use set_quantity method once product created"""
        # quantity assigned right value
        self.assertEqual(self.product1.quantity, 100)
        with self.assertRaises(clsex):
            # quantity invalid entries raises excemption
            self.product1.set_quantity(0)
            self.product1.quantity = 10.10
            self.product1.quantity = -100

    def test_is_active(self):
        """Test Initial value of product and right after buy"""
        self.assertTrue(self.product1.is_active())
        first_buy = self.product1.buy(50)
        self.assertTrue(self.product1.is_active())
        # test active and deactive case
        self.assertEqual(first_buy, 500)
        second_buy = self.product1.buy(50)
        self.assertEqual(second_buy, 500)
        self.assertFalse(self.product1.activate())
        self.assertFalse(self.product1.deactivate())
        # current quantity 0, can it be sold
        with self.assertRaises(clsex):
            self.product1.buy(1)

    def test_set_quantity(self):
        """Current quantity 0"""
        self.product1.set_quantity(100)
        # Over Product class max amount attribute value raises exception
        with self.assertRaises(clsex):
            self.product1.set_quantity(1000)
            self.product1.set_quantity(0)


if __name__ == "__main__":
    unittest.main()
