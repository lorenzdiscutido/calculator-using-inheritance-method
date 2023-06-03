class user_interface():
        
        def option(self):
            print("Calculator operations:")
            print("Type 1 if you want to use Addition(+)")
            print("Type 2 if you want to use Subtraction(-)")
            print("Type 3 if you want to use Multiplication(x)")
            print("Type 4 if you want to use Division(/)")
            print("Type 5 if you want to convert from cm to inches")
        
        def operation(self):
            option = input("Please select an operation:")
            return option
        
        def input(self):
            try:
                num = float(input("Please enter your number:"))
                return num
            except ValueError:
                print("Invalid. Please try again")
        
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
        