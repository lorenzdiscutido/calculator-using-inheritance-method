from calculator import Calculator

class lorenz_calculator(Calculator):
    pass
    def conversion(self, num1):
        print("")
        print("You chose conversion!")
        try:
            inches = num1/2.54
            print("Your number in inches is:", inches, "in")
        except (ValueError, ZeroDivisionError):
            print("Invalid. Please try again")
    
    def divide(self,num1, num2):
        print("")
        print("You chose division!")
        try:
            quotient = num2/num1
            print("The quotient of your number is:", quotient)
        except (ValueError, ZeroDivisionError):
            print("One of the number is invalid or zero. Please try again")