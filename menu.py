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
            inventory.update(features_.add_product())
        elif Ejecucion == 2:
            features_.inventory_print()
        elif Ejecucion == 3:
            print("Calculate statistics")
        elif Ejecucion == 4:
            print("Exit")
        else:
            print("Option not valid")

menu()