
# Simple item class
class ItemToPurchase:
    # parameterized constructor with default values
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    # parameterized constructor with default values
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Add Item
    def add_item(self, item):
        """
        Adds items to the cart
        input = an item object
        output = nothing, appends to cart_items
        """
        self.cart_items.append(item)

    # Remove Item
    def remove_item(self, item_name):
        """
        Removes an item from the list if it is in the list,
        otherwise it prints message
        input = an item name
        output = function returns nothing, removes item from list
        """
        found = False
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    # Modify Item
    def modify_item(self, item):
        """
        Modifies an item in the cart, if it cannot find the item it prints an error message
        input = item
        output = function returns nothing, if item not found outputs a message
        """
        found = False
        for cart_item in self.cart_items:
            if cart_item.name == item.name:
                if item.description != "none":
                    cart_item.description = item.description
                if item.price != 0:
                    cart_item.price = item.price
                if item.quantity != 0:
                    cart_item.quantity = item.quantity
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    # Get number of items in the cart
    def get_num_items_in_cart(self):
        """
        Returns the number of items in the cart
        """
        return sum(item.quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        """
        Returns the total of items in the cart in dollars
        """
        return sum(item.price * item.quantity for item in self.cart_items)

    def print_total(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Number of Items: {}".format(self.get_num_items_in_cart()))
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                print("{} {} @ ${} = ${}".format(item.name, item.quantity, item.price, item.price * item.quantity))
        print("Total: ${}".format(self.get_cost_of_cart()))

    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Item Descriptions")
        for item in self.cart_items:
            print("{}: {}".format(item.name, item.description))

# Menu method
def print_menu(cart):
    while True:
        print("\tMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")

        if choice == 'a':
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            cart.add_item(ItemToPurchase(name, description, price, quantity))
        elif choice == 'r':
            name = input("Enter item name to remove: ")
            cart.remove_item(name)
        elif choice == 'c':
            name = input("Enter item name to modify: ")
            description = input("Enter new description (or none to skip): ")
            price = input("Enter new price (or 0 to skip): ")
            quantity = input("Enter new quantity (or 0 to skip): ")
            cart.modify_item(ItemToPurchase(name, description if description != "none" else "none", 
                                            float(price) if price.isdigit() else 0, 
                                            int(quantity) if quantity.isdigit() else 0))
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid choice, please try again.")

# Main function
if __name__ == "__main__":
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    shopping_cart = ShoppingCart(customer_name, current_date)
    print_menu(shopping_cart)