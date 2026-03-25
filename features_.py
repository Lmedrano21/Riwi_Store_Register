import csv
import os
inventory = {}
products_added = {}
def validate_input_product_name(user_input):
    while user_input.strip() == "":
        print("ERROR: Product name cannot be empty. Please enter a valid product name.")
        user_input = input("Enter the name of the product: ")
    return user_input.strip()

def validate_input_price(user_input):
    validate =True
    while True:
        try:
            price = float(user_input)
            if price < 0:
                print("ERROR: Price cannot be negative. Please enter a valid price.")
                user_input = input("Enter the price of the product: ")
            elif price == 0:
                print("ERROR: Price cannot be zero. Please enter a valid price.")
                user_input = input("Enter the price of the product: ")
            elif price == "":
                print("ERROR: Price cannot be empty. Please enter a valid price.")
                user_input = input("Enter the price of the product: ") 
            else:
                validate = False
                return price
        except ValueError:
            print("ERROR: Please enter a valid numeric value for price.")
            user_input = input("Enter the price of the product: ")
                   
def validate_input_quantity(user_input):
    validate = True
    while validate:
        try:
            quantity = int(user_input)
            if quantity < 0:
                print("ERROR: Quantity cannot be negative. Please enter a valid quantity.")
                user_input = input("Enter the quantity sold: ")
            elif quantity == 0:
                print("ERROR: Quantity cannot be zero. Please enter a valid quantity.")
                user_input = input("Enter the quantity sold: ")
            elif quantity == "":
                print("ERROR: Quantity cannot be empty. Please enter a valid quantity.")
                user_input = input("Enter the quantity sold: ")
            elif quantity is type(None):
                print("ERROR: Quantity cannot be None. Please enter a valid quantity.")
                user_input = input("Enter the quantity sold: ")
            elif quantity == type(float):
                print("ERROR: Quantity must be an integer. Please enter a valid quantity.")
                user_input = input("Enter the quantity sold: ")
            else:
                validate = False
                return quantity
        except ValueError:
            print("ERROR: Please enter a valid numeric value for quantity.")
            user_input = input("Enter the quantity sold: ")                 
                   
def add_product(): #This funcition add a new product
    try:    
        producto_name = input("Enter the name of the product: ")
        producto_name = validate_input_product_name(producto_name)
        Producto_price = input("Enter the price of the product: ")
        Producto_price = validate_input_price(Producto_price)
        quantity = input("Enter the quantity: ")
        quantity = validate_input_quantity(quantity)
        
        product_added_to_saved= {
            "name": producto_name,
            "price": Producto_price,
            "quantity": quantity,
        }


        inventory = product_added_to_saved
        # CSV file name
        csv_filename = "inventory.csv"
        # Define the field names (headers)
        fieldnames = ["name", "price", "quantity"]
        # Writing to CSV
        with open(csv_filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            size = os.path.getsize("inventory.csv")
            if size == 0:
                writer.writeheader()  # Write header row
            writer.writerow(inventory)  # Write data rows
        return 
    
    except ValueError:
        print("ERROR: Please enter valid numeric values for price and quantity.")
                                    
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


def calculate_statistics():
    total = 0
    products_added_total = 0
    product_added = {}
    product_added.update(inventory)
    print("---------------------------------------------------------")
    print("Here are your statistics")
    for product, details in product_added.items():
        products_added_total += details['quantity']
        total += float((details['price'] * details['quantity']))
    print(f"The total value of the inventory is: {total}")
    print(f"The total number of products in the inventory is: {products_added_total}") 
    print("---------------------------------------------------------")
    return


