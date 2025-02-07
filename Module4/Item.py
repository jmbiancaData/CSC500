class ItemToPurchase:

    #default constructor
    def __init__(self):
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
        print("{} {} @ ${} = {:.2f}".format(self.item_name,self.item_quantity,self.item_price,self.item_total())) 