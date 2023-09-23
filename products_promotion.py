"""Should only get product instance price's value (float) and provided quantity (int) by user:
Assigned Promotion instances keeps own related values for evaluvation, instances properties' value
are provided by user and promotional assigment got done by functions.py script's promotion_managment
"""


from abc import ABC, abstractmethod


class Promation(ABC):
    """Promotion child classes only returns the total amount
    Given parameters are used for calculation. All calculation get it done
    within instance rules
    The properties of subclass may be vary, abstract class steps would be passed so
    """

    # def __init__(self, price, quantity) -> None:
    #     self.price = price
    #     self.quntity = quantity

    @abstractmethod
    def apply_promotion(self, price, quantity):
        """Abstractmethod"""


class PercentageDiscount(Promation):
    """Invoked Instance returns callculated total price
    attributes are price and quantity of product itself"""

    def __init__(self, discount_ratio) -> None:
        # super().__init__(self,price, quantity)
        self.discount_percentange = discount_ratio

    def apply_promotion(self,  price, quantity):
        """Instance attributes stores price, quantity and discount_raito values"""
        discounted_amount = price * (self.discount_percentange / 100)
        new_price = price - discounted_amount
        amount_to_pay = quantity * new_price
        return round(amount_to_pay, 2)

    def __str__(self):
        template = f"Promotion: PercentageDiscount is {self.discount_percentange}% discount"
        return template


class SecondHalfPrice(Promation):
    """Construction of class has a parameter that can be modifed
    in functions.py add_promotion method"""

    def __init__(self, steps) -> None:
        self.steps = steps

    def apply_promotion(self, price, quantity):
        """10 ve 10 geldi 10 + 5 odenecek
        4 tane 10 onluk  4/2 = 2, 2 x10 =20 + 2x5 = 100"""
        remain_from_pairs = quantity % self.steps
        half_price_amount = (quantity // self.steps) * \
            (price/self.steps)
        whole_price_amount = ((quantity // self.steps) * price) + \
            (remain_from_pairs * price)
        total_amount = half_price_amount + whole_price_amount
        return total_amount

    def __str__(self):
        template = "Promotion: SecondHalfPrice"
        return template


class ThirdOneFree(Promation):
    """One in the every trio is free similar the previous class
    it takes only one parameter that is 3"""

    def __init__(self, steps) -> None:
        self.steps = steps

    def apply_promotion(self, price, quantity):
        free_product_count = quantity // self.steps
        priceable_product_count = quantity - free_product_count + quantity % self.steps
        total_amount = priceable_product_count * price
        return total_amount

    def __str__(self):
        template = "Promotion: ThirdOneFree"
        return template

# item = PercentageDiscount(price=100, quantity=1, discount_raito=10)
# print(item.apply_promotion())
