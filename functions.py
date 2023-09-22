"""List of promotions functions"""
import ioput as io
from products_promotion import *


def get_menu():
    """Return menu desing"""
    inner_menu = """{line}
    {func}
    {items}
    {line}\n"""
    return inner_menu


def promotion_options(product: object) -> object:  # Promotion object
    """It gets product.Product type instance"""
    promotion_dict = {
        1: PercentageDiscount
    }
    number_pro = io.read_int("Enter the promotion no: ")
    if number_pro in promotion_dict:
        ratio = io.read_float("Discount percentange: ")
        # Assigns only product instance price and quantity attributes to
        # one of the product_promotion classes, avoid to change product properties
        return promotion_dict[number_pro](product.price, product.quantity, ratio)


def add_promotion(shop: object):
    """Opens up menu to display product list of store
    User enters product no to add promotion to Product
    Chosen Product.promotion attributes invokes and  get assigen
    with Promotion instance"""
    add_menu = get_menu().format(
        line="-"*6, func="LIST OF SHOP PRODUCTS", items=shop)
    product_no = io.read_int_ranged(
        f"{add_menu}\nProvide product no: ", min_value=1, max_value=len(shop.stock))
    # product assigned products.Product object
    product = shop.stock[product_no-1]
    product.promotion = promotion_options(product)
    print(product.promotion.apply_promotion())
