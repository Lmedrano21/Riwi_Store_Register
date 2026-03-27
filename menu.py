from features_ import inventory
import features_


def menu():    
    validator = True
    print("=" * 40)
    print("                 Menu")
    print("=" * 40)
    print("1- Add new product")
    print("2- Print inventory")
    print("3- Search a product")
    print("4. Update a product")
    print("5- Delete a product")
    print("6- Calculate statistics")
    print("7- Save information in CSV")
    print("8- Upload information from CSV")
    print("9- Exit")
    print("=" * 40)
    print()
    while validator:
        Ejecucion = int(input("Choose an option: "))
        if Ejecucion == 1:
            features_.add_product()
        elif Ejecucion == 2:
            features_.inventory_print()
        elif Ejecucion == 3:
             features_.search_producto()
        elif Ejecucion == 4:
            features_.product_update()
        elif Ejecucion == 5:
            features_.product_delete()
        elif Ejecucion == 6:
            features_.calculate_statistics()
        elif Ejecucion == 7:
            features_.save_csv()
        elif Ejecucion == 8:
            features_.upload_inventory_csv()
        elif Ejecucion == 9:
            print("-----------------------------------------------")
            print("Thanks for using our system! Have a great day!")
            print("-----------------------------------------------")
            validator =  False
        else:
            print("Option not valid")

