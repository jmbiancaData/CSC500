
def main():
    #Part 1

    # pseudo code:
    # ask user for 2 numbers
    # compute their sum and difference
    # display the output

    # gather user input and convert to integer
    print("\nPart 1")
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))

    # compute the sum and difference
    addition = num1 + num2
    subtraction = num1 - num2

    # display the results
    print(num1,"+",num2,"is",addition)
    print(num1,"-",num2,"is",subtraction)

    #Part 2

    # pseudo code:
    # ask user for 2 numbers
    # compute their product and quotient
    # display the output

    # gather user input and convert to integer
    print("\nPart 2")
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))

    # compute the product and quotient
    product = num1 * num2
    quotient = num1 / num2

    # display the results
    print(num1,"*",num2,"is",product)
    print(num1,"/",num2,"is",quotient)

if __name__ ==  '__main__': main()