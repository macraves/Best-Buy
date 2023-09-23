"""Test that creating a normal product works.
Test that creating a product with invalid details (empty name, negative price) invokes an exception.
Test that when a product reaches 0 quantity, it becomes inactive.
Test that product purchase modifies the quantity and returns the right output.
Test that buying a larger quantity than exists invokes exception"""

import unittest
from products import Product, QuantitativelessProducts as QP, \
    LimitedProducts as LP, ClassMethodException as clsex


class TestProducts(unittest.TestCase):
    """Creating unittest instance to check products methods"""

    def setUp(self) -> None:
        self.product1 = Product("test string", 10.0, 100)
        self.product2 = QP("  windows licence  ", price=100)
        self.product3 = LP(" limited product ", 10, 10, 2)

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

    # Test for QuantitivelessProducts
    def test_QP_name_and_quantity(self):
        """Test to initiate"""
        self.assertEqual(self.product2.name, "Windows Licence")
        self.assertTrue(self.product2.quantity, 1)

    def test_QP_set_quantity(self):
        """Attemt to set quantity or
        none integer values raises exception"""
        with self.assertRaises(clsex):
            self.product2.quantity = 2
            self.assertFalse(self.product2.quantity, 2)
            self.product2.set_quantity(1)
            self.product2.set_quantity("None")

    def test_QP_buy_method(self):
        """More than 1 to buy raises exeption"""
        with self.assertRaises(clsex):
            self.product2.buy(1)
            self.product2.buy("None")

    def test_QP_always_Active(self):
        """Prevent Any attemt to change active to not active preventation"""
        self.assertTrue(self.product2.is_active())
        # QP products can not be set as False
        with self.assertRaises(clsex):
            self.product2.active = False
            self.product2.deactivate()
    # TEST FOR LimitedProduct as LP product3

    def test_LP_name(self):
        """Test the product name"""
        # self.product3 = LP(" limited product ", 10, 10, 2)
        self.assertTrue(self.product3.name, "Limited Product")

    def test_lp_allowed_number_methods(self):
        """Test the allowed purchase count getter and setter"""
        self.assertEqual(self.product3.allowed_ship_count, 2)
        # Raise Exception situations:
        with self.assertRaises(clsex):
            self.product3.allowed_ship_count = None
            self.product3.allowed_ship_count = ""

    def test_lp_buy_methods(self):
        """Test LP buy method"""
        test_product = LP("allowed purchased is 2", 10, 10, 2)
        with self.assertRaises(clsex):
            # test if buy arguments is none integer
            self.product3.buy("")
        # Test if test_product can be executed 3 times
        total_amount = test_product.buy(1)
        total_amount += test_product.buy(1)
        with self.assertRaises(clsex):
            total_amount += test_product.buy(1)

        self.assertTrue(total_amount, 20)


if __name__ == "__main__":
    unittest.main()
