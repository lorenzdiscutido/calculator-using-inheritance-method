from calculator import Calculator
from user_interface import user_interface

calc = Calculator()
ui = user_interface()

class lorenz_calculator(calc):
    def conversion(self):
        cm = float(input("Please enter a number in cm"))
        inches = cm/2.54
        return inches