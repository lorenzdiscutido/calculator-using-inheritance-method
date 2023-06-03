from calculator import Calculator

class lorenz_calculator(Calculator):
    pass
    def conversion(self, num1):
        print("")
        print("You chose conversion!")
        try:
            inches = num1/2.54
            print("Your number in inches is:", inches, "in")
        except:
            print("Invalid. Please try again")
    
    def divide(self)