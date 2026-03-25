def inventory_print():
    total_records = {}
    total_records.update(inventory)
    
    
    with open('inventory.csv', mode ='r') as file:    
        csvFile = csv.DictReader(file)
        print("Here are your inventory")
        for lines in csvFile:
            print(f"Product name: {lines['name']}")
            print(f"Product price: {lines['price']}")
            print(f"Product quantity: {lines['quantity']}")
            print("---------------------------------------------------------")

            

    
    print("---------------------------------------------------------")
    print("Exiting the inventory management system.")
    return

#this is the code from the function about print the inventory before i try the new code, 