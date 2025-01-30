# Part 1

# Variables given in part 1
tip = .18
tax = .07

# prompt user for the subtotal of the meal
subtotal = float(input("What is the subtotal: "))

# calculate various amounts that will be displayed on the receipt
tip_amount = subtotal * tip
total_before_tip = subtotal * ( 1 + tax)
total_tax = subtotal * tax
total = total_before_tip + tip_amount

# print the receipt with normalized percentages for tax and tip
print("\nReciept")
print("Subtotal: {:.2f}".format(subtotal))
print("{:.0f}% tip : {:.2f}".format(tip * 100,tip_amount))
print("{:.0f}% sales tax: {:.2f}".format(tax * 100, total_tax))
print("Total before tip: {:.2f}".format(total_before_tip))
print("Total with tax and tip: {:.2f}".format(total))