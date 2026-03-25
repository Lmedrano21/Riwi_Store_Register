from features_ import inventory
import features_


def menu():    
    validator = True
    print("=" * 40)
    print("                 Menu")
    print("=" * 40)
    print("1- Add new product")
    print("2- Print inventory")
    print("3- Calculate statistics")
    print("4- Exit")
    print("=" * 40)
    print()
    while validator:
        Ejecucion = int(input("Choose an option: "))
        if Ejecucion == 1:
            print("Add new product")
            features_.add_product()
        elif Ejecucion == 2:
            features_.inventory_print()
        elif Ejecucion == 3:
            features_.calculate_statistics()
        elif Ejecucion == 4:
            print("-----------------------------------------------")
            print("Thanks for using our system! Have a great day!")
            print("-----------------------------------------------")
            validator =  False
        else:
            print("Option not valid")

