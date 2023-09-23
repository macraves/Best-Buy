""" Store Class Properties and Behaviours"""
import products


class StoreExceptions(Exception):
    """Handles Store Class matter exceptions"""

    def __init__(self, store_message: object) -> None:
        super().__init__(store_message)


class Store:
    """Creating of properties"""

    def __init__(self, product_list) -> None:
        self.stock = product_list

    def add_product(self, product: object):
        """Adding Product class instance to stock list"""
        if not isinstance(product, products.Product):
            raise StoreExceptions("Requested product type is not valid")
        self.stock.append(product)

    def remove_product(self, product: object) -> str:
        """Uses remove method of list to remove product from the list"""
        if len(self.stock) == 0:
            raise StoreExceptions("Stoke is empty")
        if not isinstance(product, products.Product):
            raise StoreExceptions("Requested product type is not valid")
        if product not in self.stock:
            raise StoreExceptions("Product not in the list")
        self.stock.remove(product)
        return "Product is removed"

    def get_total_quantity(self):
        "Returns how many items are in the store in total"
        total_quantity = sum(product.quantity for product in self.stock)
        return total_quantity

    def get_all_products(self) -> list:
        """Returns all products in the store that are active"""
        active_items = list(filter(lambda item: item.is_active(), self.stock))
        return active_items

    def __str__(self) -> str:
        """Return Saved all products in the store
        Regarless is active or not"""
        products_list_string = "\n".join(
            f"{count}. {item}" for count, item in enumerate(self.stock, start=1)
        )
        return products_list_string


def test_remove_product():
    """Returns how many items are in the store in total"""
    items_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                  products.Product("Bose QuietComfort Earbuds",
                                   price=250, quantity=500),
                  products.Product("Google Pixel 7",
                                   price=500, quantity=250),
                  ]
    phone = products.Product("Samsung S10",
                             price=100, quantity=100)
    store = Store(product_list=items_list)
    store.add_product(phone)
    # active_products = store.get_all_products()
    return store


if __name__ == "__main__":
    test_remove_product()
