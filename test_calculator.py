from lorenz_calculator import lorenz_calculator
from ui import user_interface

LC = lorenz_calculator()
ui = user_interface()

ui.option()

while True:
    num1 = ui.input()
    num2 = ui.input() 

    option = ui.operation()

    if option == "1":
        sum = LC.add(num1, num2)
    elif option == "2":
        difference = LC.subtract(num1, num2)
    elif option == "3":
        product = LC.multiply(num1, num2)
    elif option == "4":
        quotient = LC.divide(num1, num2)
    elif option == "5":
        convert = LC.conversion(num1)
        convert1 = LC.conversion(num2)
    else:
        print("Invalid choice. Please enter another one")

    if not ui.again():
        break

