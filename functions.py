"""List of promotions functions"""

import ioput as io
from products_promotion import PercentageDiscount, SecondHalfPrice, ThirdOneFree


class NoPromitionValue(Exception):
    """To stop Inner loop"""

    def __init__(self, message) -> None:
        super().__init__(message)


def get_template():
    """Return menu desing"""
    inner_menu = """{line}
{title}
{items}
{line}"""
    return inner_menu


def promotion_managment(chosen_product) -> object:  # Promotion object
    """According the user choice create Promotion instance 
    Instance's properties are provided by user
    Returns:
        object: Promotion type instance gets assigned to property of: product.promotion
    """

    if chosen_product.promotion is None:
        promotion_options = {
            1: PercentageDiscount,
            2: SecondHalfPrice,
            3: ThirdOneFree
        }

        promotion_map = map(lambda double: f"{double[0]}: {str(double[1].__name__)}", enumerate(
            promotion_options.values(), start=1))
        promotion_template = "\n".join(promotion_map)

        promotion = io.read_int_ranged(
            promotion_template + "\n\nEnter the promotion no: ",
            min_value=1, max_value=len(promotion_options))
        if promotion == 1:
            ratio = io.read_float("Discount percentange: ")
            return promotion_options[promotion](ratio)
        if promotion == 2:
            step_for_half_price = 2
            return promotion_options[promotion](step_for_half_price)
        if promotion == 3:
            step_to_free = 3
            return promotion_options[promotion](step_to_free)
    else:
        if io.ask_to_continue(
                f"""Product info:
            {chosen_product} 
            It has already been promoted
            Do you want to delete it y/n? """):
            # assigns None to produc.promotion property
            chosen_product.promotion = None
        else:
            # if user decided to keep current promotion it will return it back
            return chosen_product.promotion


def remove_management(product):
    """to not change all convention"""
    if product.promotion is None:
        raise NoPromitionValue(
            "The product does not have any promotion to remove")
    product.promotion = None

    return product.promotion


def product_list_iner_loop(shop: object, function, menu_title, action):
    """That will execute function method as user requested"""
    while True:
        add_menu = get_template().format(
            line="*"*len(menu_title), title=menu_title, items=shop)
        product_no = io.read_int_ranged(
            f"{add_menu}\nSelect a product to {action} a promotion: ",
            min_value=1, max_value=len(shop.stock))
        # product variable is assigned products.Product object by user entry
        product = shop.stock[product_no-1]
        # promotion property gets its value as Promotion type
        try:
            product.promotion = function(product)
        except NoPromitionValue as npv:
            print(f"{npv}".upper())
            break
        if not io.ask_to_continue(f"Do you want to {action} another promotion y/n? "):
            break


def add_promotion(shop: object):
    """Opens up menu to display product list of store
    User enters product no to add promotion to Product
    Chosen Product.promotion attributes invokes and  get assigen
    with Promotion instance"""
    menu_title = "PROMOTION MANAGMENT"
    action_name = "ADD"
    product_list_iner_loop(shop, promotion_managment, menu_title, action_name)
    # while True:
    #     add_menu = get_template().format(
    #         line="*"*len(menu_title), title=menu_title, items=shop)
    #     product_no = io.read_int_ranged(
    #         f"{add_menu}\nSelect product to get promoted: ", min_value=1, max_value=len(shop.stock))
    #     # product variable is assigned products.Product object by user entry
    #     product = shop.stock[product_no-1]
    #     # promotion property gets its value as Promotion type
    #     product.promotion = promotion_managment(product)
    #     if not io.ask_to_continue("Do you want to add another promotion y/n? "):
    #         break


def show_product_details(shop):
    """iterate through in shop.stock list to find the product by name"""
    search_result = None
    product_name = io.read_text("Please enter the product name: ")
    product_name = product_name.strip().title()
    for product in shop.stock:
        if product_name in product.name:
            search_result = product
    if search_result is not None:
        print(f"\nFound Product according your entry:\n{search_result}\n")
    else:
        print(f"\n{product_name} is not found in the stock\n")


def remove_promotion(shop: object) -> None:
    """This method has been already in promotion managment
    as the project ask for this method add promotion inner loop will be another method"""
    action_name = "REMOVE"
    remove_title = "REMOVE PROMOTION"
    product_list_iner_loop(shop, remove_management, remove_title, action_name)


def validate_user_answer():
    """Returns list of lists, nested list first index is product index
    nested list second index amount to buy
    Ignores non integer base entries
    """
    questions = ["Which product # do you want? ", "What amount do you want? "]
    basket = []
    while True:
        answers = []
        for question in questions:
            answer = input(question)
            if answer.isnumeric():
                answer = int(answer)
            answers.append(answer)
        # Eliminate non integer entry
        is_any_not_int = any(not isinstance(item, int) for item in answers)
        if is_any_not_int:
            break
        basket.append(answers)
    return basket
