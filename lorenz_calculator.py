from calculator import Calculator

class lorenz_calculator(Calculator):
    pass
    def conversion(self, num1):
        print("")
        print("you chose conversion")
        try:
            inches = num1/2.54
            print(inches)
        except:
            print("Invalid. Please try again")
            return inches