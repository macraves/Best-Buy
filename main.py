"""USER INTERFACE"""
import store
import products
import ioput as io
from functions import *


def default_inventory() -> object:
    """To Test default items would be added to the store"""
    items_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                  products.Product("Bose QuietComfort Earbuds",
                                   price=250, quantity=500),
                  products.Product("Google Pixel 7",
                                   price=500, quantity=250),
                  ]
    test_store = store.Store(items_list)
    # Adding one more item
    phone = products.Product("samsung S10",
                             price=100, quantity=100)
    test_store.add_product(phone)
    return test_store


TEST_STORE = default_inventory()


# PROMOTIONS
# ARE USED TO BE HERE

def list_store_products(stored: object) -> None:
    """Use Store object __str__ method"""
    menu_title = "LIST OF STORE PRODUCTS"
    inner_menu_view = get_template().format(
        line="-"*len(menu_title), title=menu_title, items=stored)
    print(inner_menu_view)


def total_amount_in_store(stored: object) -> None:
    """Total quantities of all products"""
    menu_title = "TOTAL AMOUNT OF PRODUCTS"
    total_amount = sum(item.quantity for item in stored.stock)
    total_view = f"{'-'*len(menu_title)}\n{menu_title}: {total_amount}\n{'-'*len(menu_title)}"
    print(total_view)


def make_an_order(stored) -> None:
    """Gets user base entry (index, amount to buy)
    Matches index -1 from available products list"""
    products_cost = 0
    available_products = stored.get_all_products()  # list of object
    if not available_products:
        print("\nStoke is empty\n")
        return ""
    available_products_string_list = [
        str(product) for product in stored.get_all_products()]
    # enumerate index starts from 1, real index is 0
    availables_str = "\n".join(f"{count}. {item}" for count, item in enumerate(
        available_products_string_list, start=1))
    menu_title = "AVAILABLE PRODUCTS"
    inner_menu_view = get_template().format(
        line="$"*len(menu_title), title=menu_title, items=availables_str)
    print(inner_menu_view)
    chosen_products = validate_user_answer()
    # list of lists, lists first value is index, second value quantity of request
    if chosen_products:
        for item in chosen_products:
            item_index = item[0] - 1
            item_requested_quantity = item[1]
            product = available_products[item_index]
            try:
                product_cost = product.buy(item_requested_quantity)
                products_cost += product_cost
                print("Product added to list!")
            except products.ClassMethodException as clsmex:
                print(
                    f"Error while making order! {clsmex}")
        if products_cost > 0:
            print(f"\n{'='*18}\nORDER MADE, TOTAL: {product_cost}\n{'='*18}\n")
    else:
        print(
            "Neither the Store object is empty, nor did the user enter appropriate data.")


def remove_product_in_stock(test_store: object) -> bool:
    """Usage of Store.remove_product method"""
    menu_title = "REMOVING - PRDOCUT"
    while test_store.stock:
        inner_menu_view = get_template().format(
            line="X"*len(menu_title), title=menu_title, items=test_store)
        product_no = io.read_int_ranged(
            f"{inner_menu_view}\nProvide product no: ",
            min_value=1, max_value=len(test_store.stock))
        try:
            product = test_store.stock[product_no-1]
            print(test_store.remove_product(product))
        except store.StoreExceptions as sexc:
            print(f"Error during the removal {sexc}")
        if not io.ask_to_continue("DO YOU WANT TO REMOVE ANOTHER PRODUCT y/n? "):
            break
    print("\nLIST IS EMPTY")


def add_new_product(test_store):
    """ADDING MENU"""
    menu = "PLEASE CHOSE PRODUCT TYPE"
    adding_menu = """\n\t{title}\n\t{line}
    1: "Product",
    2: "Products without quantity",
    3: "Limited Product"
Please choice one of the options above: """.format(line='+'*len(menu), title=menu)
    while True:
        adding_choice = io.read_int_ranged(
            adding_menu, min_value=1, max_value=3)
        try:
            product_name = io.read_text("Provide product name: ")
            product_price = io.read_float("Provide product price: ")
            if adding_choice == 1:
                product_quantity = io.read_int("Provide product quantity: ")
                new_product = products.Product(
                    product_name, product_price, product_quantity)
            elif adding_choice == 2:
                new_product = products.QuantitativelessProducts(
                    product_name, product_price)
            elif adding_choice == 3:
                product_quantity = io.read_int("Provide product quantity: ")
                product_limitations = io.read_int(
                    "Provide product limitations: ")
                new_product = products.LimitedProducts(
                    product_name, product_price, product_quantity, product_limitations)
        except products.ClassMethodException as cme:
            print(f"Adding failed: {cme}\nPlease try again")
            continue
        test_store.stock.append(new_product)
        print("New product added to Store Stock")
        if not io.ask_to_continue("DO YOU WANT TO ADD ANOTHER PRODUCT y/n: "):
            break


def opening_scene(test_store):
    """Designs User Interface"""
    title = "OPERATION MENU"
    line = "-"*len(title)
    menu = f"""\t{title}\n\t{line}
1. List all products in store
2. Show total amount in store
3. Add new product in store
4. Remove a product in store
5. Add promotion
6. Remove promotion
7. Show product details
8. Make an order
9. Quit
Please provide a operation number: """
    functions = {
        1: list_store_products,
        2: total_amount_in_store,
        3: add_new_product,
        4: remove_product_in_stock,
        5: add_promotion,
        6: remove_promotion,
        7: show_product_details,
        8: make_an_order,
        9: "quit"
    }
    while True:
        menu_choice = io.read_int_ranged(menu, min_value=1, max_value=9)
        function = functions[menu_choice]
        if function == "quit":
            break
        function(test_store)


def main():
    """Main Flow"""
    opening_scene(TEST_STORE)


if __name__ == "__main__":
    main()
