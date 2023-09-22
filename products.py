"""Product properties and behaivours"""
import products_promotion as pp


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
        self.promotion = {}
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
        if not isinstance(entered_name, str) or len(entered_name.strip()) == 0:
            raise ClassMethodException("Please enter text")
        self._name = entered_name.lower().title().strip()

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

    def set_promotion(self, promotion):
        """Product instance promotion attributes is assigned to 
        the Promotion instance"""
        self.promotion = promotion

    @classmethod
    def validate_buyer_quantity(cls, buyer_request: int) -> bool:
        """Validates buyer request quantity"""
        if not isinstance(buyer_request, int):
            raise ClassMethodException("Buying quantity must be integer")
        return 0 <= buyer_request <= cls._max_customer_request

    def buy(self, quantity) -> float:
        """Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        Invalid entry raises an Exception"""
        if not Product.validate_buyer_quantity(quantity):
            raise ClassMethodException(
                f"Invalid Buyer request\nMaximum Customer Request: {Product._max_customer_request}")
        if quantity > self.quantity:
            raise ClassMethodException(
                f"Quantity larger than what exists\nAvailable amount is {self.quantity}")
        if self.promotion:
            # return total price
            pass
        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            Product.deactivate(self)
        return total_price


class QuantitativelessProducts(Product):
    """Only share name and price attributes
       Quantity need to be set on 1 in his definition
       Attempt to get setted should raise exception, override to super buy
       Buy methods only accept 1 as quantity
       Products alwasy active
            **instance attribute active cannot be manupilated for that
                getter and setter method override super active attribute
            **deactivation of instance attribute active calls the exception
            ** Attempt to set quantity any other number other than 1 prevented"""

    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, price, quantity=1)

    # Overriding some super class spesific methods according
    # quantitive less producs behaivours
    @property
    def quantity(self) -> float:
        return 1

    @quantity.setter
    def quantity(self, value):
        if value != 1:
            raise ClassMethodException(
                f"{self.name}`s quantity cannot be andy digit rather than 1 ")

    def set_quantity(self, quantity) -> None:
        if isinstance(quantity, int):
            raise ClassMethodException(
                f"{self.name}, This Product Quantity cannot be setted")

    def buy(self, quantity) -> float:
        """Buying more than 1 raises exception"""
        if quantity != 1:
            raise ClassMethodException(
                f"{self.name} Attempt to any number rather than 1")
        return super().buy(1)
    # Overide instance attribute "active"

    @property
    def active(self) -> bool:
        """Always considered return True"""
        return True

    @active.setter
    def active(self, value):
        if not value:
            raise ClassMethodException(f"{self.name} cannot be deactivated")

    def deactivate(self):
        raise ClassMethodException(f"{self.name} cannot be deactivated ")

    def is_active(self) -> bool:
        """It returns always True for Quantitave less"""
        return True


class LimitedProducts(Product):
    """Limited products must have exclusively purchase info
    Atttemp to order more than purchase count must get under control
    child class buy methods"""

    def __init__(self, name: str, price: float, quantity: int, count) -> None:
        super().__init__(name, price, quantity)
        # Use a different name for the instance variable
        self._allowed_purchase_count = count
        self.purchased_number = 0

    @property
    def allowed_purchase_count(self):
        """Getter Method"""
        return self._allowed_purchase_count

    @allowed_purchase_count.setter
    def allowed_purchase_count(self, quantity):
        if not isinstance(quantity, int):
            raise ClassMethodException("Invalid purchase quantity")
        if quantity > self.quantity:
            raise ClassMethodException("There is not enough quantity")
        self._allowed_purchase_count = quantity

    def buy(self, quantity):
        """Checks instance purchase count by its own allowed count
        if purchase get greater value than instance attribute it prints message
        and it will not execute last order but it returns 0"""
        if Product.validate_buyer_quantity(quantity):
            if self.allowed_purchase_count == self.purchased_number:
                print(
                    f"{self.name} product, cannot be ordered more than {self.allowed_purchase_count}")
                return 0
            self.purchased_number += 1
            return super().buy(quantity)
