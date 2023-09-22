"""USER INTERFACE"""
import store
import products
import ioput as io

# Ctrl + Enter Run the cell but not advencing
INNER_MENU_VIEW = """{line}
{func}
{items}
{line}\n"""


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


def list_store_products(stored: object) -> None:
    """Use Store object __str__ method"""
    inner_menu_view = INNER_MENU_VIEW.format(
        line="-"*6, func="LIST OF STORE PRODUCTS", items=stored)
    print(inner_menu_view)


def total_amount_in_store(stored: object) -> None:
    """Total quantities of all products"""
    total_amount = sum(item.quantity for item in stored.stock)
    print(f"Total of {total_amount} items in store")


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
    make_order_view = INNER_MENU_VIEW.format(
        line="-"*6, func="AVAILABLE PRODUCTS", items=availables_str)
    print(make_order_view)
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
            print(f"Order made! Total payment: ${products_cost}")
    else:
        print(
            "Neither the Store object is empty, nor did the user enter appropriate data.")


def add_product():
    """ADDING MENU"""
    adding_menu = '''
        1: "Product",
        2: "Products without quantity",
        3: "Limited Product"
    Please choice one of the options above: '''
    adding_choice = io.read_int_ranged(adding_menu, min_value=1, max_value=3)

    if adding_choice == 1:
        product_name = io.read_text("Provide product name: ")
        product_price = io.read_float("Provide product price: ")
        product_quantity = io.read_int("Provide product quantity: ")
        new_product = products.Product(
            product_name, product_price, product_quantity)
    elif adding_choice == 2:
        product_name = io.read_text("Provide product name: ")
        product_price = io.read_float("Provide product price: ")
        new_product = products.QuantitativelessProducts(
            product_name, product_price)
    elif adding_choice == 3:
        product_name = io.read_text("Provide product name: ")
        product_price = io.read_float("Provide product price: ")
        product_quantity = io.read_int("Provide product quantity: ")
        product_limitations = io.read_int("Provide product limitations: ")


def opening_scene(TEST_STORE):
    """Designs User Interface"""
    menu_title = "Store Menu"
    line = "-" * len(menu_title)
    menu = f"""{menu_title}
{line}
1. List all products in store
2. Show total amount in store
3. Add new product in store
4. Remove a product in store
5. Add promotion
6. Remove promotion
7. Show product details
8. Make an order
9. Quit
Please choose a number: """
    functions = {
        1: list_store_products,
        2: total_amount_in_store,
        3: "add_new_product",
        4: "remove_product",
        5: "add_promotion",
        6: "remove_promotion",
        7: "show_product_details",
        8: make_an_order,
        9: "quit"
    }
    while True:
        menu_choice = io.read_int_ranged(menu, min_value=1, max_value=9)
        function = functions[menu_choice]
        if function == "quit":
            break
        function(TEST_STORE)


def main():
    """Main Flow"""
    TEST_STORE = default_inventory()
    opening_scene(TEST_STORE)


if __name__ == "__main__":
    main()
