class Calculator:

    def add(self, num1, num2):
        print("")
        print("You chose Addition as your operation")
        try:
            sum = num1 + num2
            print("The sum of the two number is:", sum)
        except ValueError:
            print("Invalid. Please try again")  

    def subtract(self, num1, num2):
        print("")
        print("You chose Subtraction as your operation")
        try:
            difference = num1 -num2
            print("The difference of the two number is:", difference)
        except ValueError:
            print("Invalid. Please try again")

    def multiply(self, num1, num2):
        print("")
        print("You chose Multiplication as your operation")
        try:
            product = num1*num2
            print("The product of the two number is:", product)
        except ValueError:
            print("Invalid. Please try again")

    def divide(self, num1, num2):
        print("")
        print("You chose Division as your operation")
        try:
            quotient = num1/num2
            print("The quotient of the two number is", quotient)
        except (ValueError, ZeroDivisionError):
            print("Invalid. Please try again")
 
    
    