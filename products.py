"""Product properties and behaviours"""


class ClassMethodException(Exception):
    """Handles Product Class matters exceptions"""

    def __init__(self, message: object) -> Exception:
        super().__init__(message)


class Product:
    """initialising class properties"""
    _max_stock_entry: int = 2000
    _max_customer_request: int = 600

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        if self.quantity == 0:
            self.active: bool = False
        else:
            self.active: bool = True

    @property
    def name(self) -> str:
        """name getter method"""
        return self._name

    @name.setter
    def name(self, entered_name):
        """Ignore invalid name entry and capitilaze string"""
        if not isinstance(entered_name, str):
            raise ClassMethodException("Please enter text")
        self._name = entered_name.lower().title()

    @property
    def quantity(self) -> float:
        """Getter function for quantity Returns the quantity (float)"""
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Quantity setter"""
        if not isinstance(quantity, int):
            raise ClassMethodException("Invalid quantity entry")
        if quantity < 0:
            raise ClassMethodException("Quantity cannot be negative")
        self._quantity = quantity

    def set_quantity(self, quantity) -> None:
        """Setter function for quantity. If quantity reaches 0, deactivates the product"""
        if quantity > Product._max_stock_entry:
            raise ClassMethodException(
                f"Invalid Stock Entry\nMax stock entry is: {Product._max_stock_entry}")
        if quantity == 0:
            raise ClassMethodException(
                "Quantity cannot set 0 from outside scope")
        self.quantity += quantity

    def is_active(self) -> bool:
        """Getter function for active. Returns True if the product is active, otherwise False"""
        return self.quantity > 0

    def activate(self):
        """Activates the product"""
        self.active = True

    def deactivate(self):
        """Deactivates the product"""
        self.active = False

    def __str__(self) -> str:
        """Product object string representation"""
        template = f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"
        return template

    @classmethod
    def validate_buyer_quantity(cls, buyer_request: int) -> bool:
        """Validates buyer request quantity"""
        return 0 <= buyer_request <= cls._max_customer_request

    def buy(self, quantity) -> float:
        """Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        Invalid entry raises an Exception"""
        if quantity > self.quantity:
            raise ClassMethodException(
                f"Quantity larger than what exists\nAvailable amount is {self.quantity}")
        if not Product.validate_buyer_quantity(quantity):
            raise ClassMethodException(
                f"Invalid Buyer request\nMaximum Customer Request: {Product._max_customer_request}")
        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            Product.deactivate(self)
        return total_price


def test_product_class():
    """Test of product class"""
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose)
    print(mac)

    bose.set_quantity(1000)
    print(bose)


if __name__ == "__main__":
    test_product_class()
