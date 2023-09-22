"""Should only get product instance price and quantity attributes values:
Only instance reference, Because Promotion classes should not be able to
change product instance properties"""


from abc import ABC, abstractmethod


class Promation(ABC):
    """Logic of Promotion"""

    def __init__(self, price, quantity) -> None:
        self.price = price
        self.quntity = quantity

    @abstractmethod
    def apply_promotion(self):
        """Abstractmethod"""


class PercentageDiscount(Promation):
    """Invoked Instance returns callculated total price
    attributes are price and quantity of product itself"""

    def __init__(self, price, quantity, discount_raito) -> None:
        super().__init__(price, quantity)
        self.discount_percentange = discount_raito

    def apply_promotion(self):
        """Instance attributes stores price, quantity and discount_raito values"""
        discount = (self.price * self.discount_percentange) / 100
        promotioned_price = self.price * self.quntity * discount
        return promotioned_price


class SecondHalfPrice(Promation):
    pass


class ThirdOneFree(Promation):
    pass
