# Portfolio Milestone
# import class from our library
from Item import ItemToPurchase

def main():
    # Item 1
    name = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    quant = int(input("Enter the item quantity: "))

    # Parameterized Constructor
    item1 = ItemToPurchase( name, price, quant ) 

    # Item 2
    name = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    quant = int(input("Enter the item quantity: "))

    # Parameterized Constructor
    item2 = ItemToPurchase( name, price, quant )

    # Output
    print("Total Cost")
    item1.print_item_cost()
    item2.print_item_cost()
    print('Total: ${:.2f}'.format(item1.item_total() + item2.item_total()))

if __name__ == '__main__':
    main()
