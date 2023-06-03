#Create a class named calculator
class Calculator:

    #Show the user what to enter to use operation
    def option(self):
        print("Calculator operations:")
        print("Type 1 if you want to use Addition(+)")
        print("Type 2 if you want to use Subtraction(-)")
        print("Type 3 if you want to use Multiplication(x)")
        print("Type 4 if you want to use Division(/)")
    
    #add a function that will ask the user what operation they like to use
    def operation(self):
        option = input("Please select an operation:")
        return option
    #Add a function that ask the user to input two numbers
    def input(self):
        try:
            num = float(input("Please enter your number:"))
            return num
        except ValueError:
            print("Invalid. Please try again")
    #Add a function that add the two numbers
    def add(self, num1, num2):
        print("")
        print("You chose Addition as your operation")
        try:
            sum = num1 + num2
            print("The sum of the two number is:", sum)
        except ValueError:
            print("Invalid. Please try again")  

    #Add a function that subtract the two numbers
    def subtract(self, num1, num2):
        print("")
        print("You chose Subtraction as your operation")
        try:
            difference = num1 -num2
            print("The difference of the two number is:", difference)
        except ValueError:
            print("Invalid. Please try again")

    #Add a function that multiply the two numbers
    def multiply(self, num1, num2):
        print("")
        print("You chose Multiplication as your operation")
        try:
            product = num1*num2
            print("The product of the two number is:", product)
        except ValueError:
            print("Invalid. Please try again")

    #Add a function that divide the two numbers
    def divide(self, num1, num2):
        print("")
        print("You chose Division as your operation")
        try:
            quotient = num1/num2
            print("The quotient of the two number is", quotient)
        except (ValueError, ZeroDivisionError):
            print("Invalid. Please try again")

    #Add a function that ask the user if they want to retry the calculation
    def again(self):
        while True:
            retry = input("Do you want to retry?(y/n)")
            if retry.lower() == "n":
                print("")
                print("Thank you for using this calculator")
                print("")
                return False
            elif retry.lower() == "y":
                print("")
                print("Proceeding to another calculation...")
                return True
            else:
                print("Invalid input. Please try again")
    
    
    