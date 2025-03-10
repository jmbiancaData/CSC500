# Portfolio Milestone

class ItemToPurchase:

    # default constructor
    def __init__(self):
        # attributes
        self.item_name = 'none'
        self.item_price = 0.0
        self.item_quantity = 0

    # parameterized constructor
    def __init__(self,name,price,quantity):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity

    def item_total(self):
        return self.item_price * self.item_quantity
    
    def print_item_cost(self):
        print("{} {} @ ${:.2f} = {:.2f}".format(self.item_name,self.item_quantity,self.item_price,self.item_total())) 

def main():
    # Item 1
    name = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    quant = int(input("Enter the item quantity: "))
    # formatting
    print()
    # Parameterized Constructor
    item1 = ItemToPurchase( name, price, quant ) 

    # Item 2
    name = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    quant = int(input("Enter the item quantity: "))
    # formatting 
    print()
    # Parameterized Constructor
    item2 = ItemToPurchase( name, price, quant )

    # Output
    print("Total Cost")
    item1.print_item_cost()
    item2.print_item_cost()
    print('Total: ${:.2f}'.format(item1.item_total() + item2.item_total()))

if __name__ == '__main__':
    main()
