import csv
import os
global inventory, inventory_for_csv, inventory_from_csv
inventory = {}
inventory_for_csv = {}
inventory_from_csv = {}
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
    product_added_to_saved={}
    try:    
        producto_name = input("Enter the name of the product: ")
        producto_name = validate_input_product_name(producto_name)
        Producto_price = input("Enter the price of the product: ")
        Producto_price = validate_input_price(Producto_price)
        quantity = input("Enter the quantity: ")
        quantity = validate_input_quantity(quantity)
        
        product_added_to_saved[producto_name]= {
            "name": producto_name,
            "price": Producto_price,
            "quantity": quantity,
        }
        inventory.update(product_added_to_saved)
                
        product_added_to_saved_csv= {
            "name": producto_name,
            "price": Producto_price,
            "quantity": quantity,
        }
        inventory_for_csv.update(product_added_to_saved_csv)
        print("Product added succesfullly")
        return 
    except ValueError:
        print("ERROR: Please enter valid numeric values for price and quantity.")

def save_csv(): #function #7
    # CSV file name
    csv_filename = "inventory.csv"
    # Define the field names (headers)
    fieldnames = ["name", "price", "quantity"]
    # Writing to CSV
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction='ignore')
        size = os.path.getsize("inventory.csv")
        if size == 0:
            writer.writeheader()  # Write header row
        writer.writerow(inventory_for_csv)  # Write data rows
    print("CSV file is saved succesfully")
    return 

def inventory_print():
    total_records = {}
    total_records.update(inventory)
    print("---------------------------------------------------------")
    print("Here are your inventory")
    for product, details in total_records.items():
        print(f"Product: {product}")
        print(f"  Price: {details['price']}")
        print(f"  Quantity: {details['quantity']}")
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("Exiting the inventory management system.")
    return

def search_producto():
    name_to_search = input("Please input the name's product to search: ")

    producto_info = inventory.get(name_to_search)
    if producto_info:
        print(f"Information: ")
        print(f"Name: {producto_info['name']}")
        print(f"Price: {producto_info['price']}")
        print(f"Quantity: {producto_info['quantity']}")
        print("---------------------------------------------------------")
    else:
        print(f"The product '{name_to_search}' is not found, please try again.")
        print("---------------------------------------------------------")
        
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

def product_update():
    name_to_search = input("Please input the name's product to update: ")

    producto_info = inventory.get(name_to_search)
    
    if not producto_info:
        print(f" Product '{producto_info['name']}' not found.")
        return 
    

    print(f"\nUpdate: {producto_info['name']} (Price: {producto_info['price']}, Stock: {producto_info['quantity']})")
    print("1. Change Price")
    print("2. Change Stock")
    print("3. Change Both")
    
    option = input("Choose an option: ")

    if option == "1":
        producto_info["price"] = float(input("New price: "))
    elif option == "2":
        producto_info["quantity"] = int(input("New stock: "))
    elif option == "3":
        producto_info["price"] = float(input("New price: "))
        producto_info["quantity"] = int(input("New stock: "))
    else:
        print("Invalid option.")
        
    print(" Update successful.")
    return 

def product_delete():
    name = input("Enter the name of the product you wish to delete: ")
    if name in inventory:
        confirmar = input(f" Are you sure you want to delete '{name}'? (Yes/No): ").lower()
        
        if confirmar == 'yes':
            del inventory[name]
            print(f" The product '{name}' has been successfully deleted.")
            return 
        else:
            print(" Operation cancelled by the user")
            return 
    else:
        print(f" Error: The product '{name}' does not exist in the inventory.")
        return 


def upload_inventory_csv(route="new_inventory.csv"):
    invalid_rows = 0
    csv_data = {} # Usamos un dict temporal para los nuevos datos
    
    try:
        with open(route, 'r', encoding='utf-8') as csvfile:
            result = csv.reader(csvfile)
            try:
                header = next(result)
            except StopIteration:
                print("The file is empty.")
                return

            if header != ['name', 'price', 'quantity']:
                print("The CSV header is invalid. Expected: name, price, quantity")
                return

            for fila in result:
                # Validar que existan las 3 columnas y no estén vacías
                if len(fila) == 3 and all(item.strip() for item in fila):
                    try:
                        name = fila[0].strip()
                        price = float(fila[1])
                        quantity = int(fila[2])

                        if price > 0 and quantity > 0:
                            csv_data[name] = {'price': price, 'quantity': quantity}
                        else:
                            invalid_rows += 1
                    except ValueError:
                        invalid_rows += 1
                else:
                    invalid_rows += 1
                    
        if not csv_data:
            print("No valid data was found to load.")
            return

        while True:
            option = input("\nDo you want to overwrite the entire current inventory? (Y/N): ").strip().upper()
            if option in ["Y", "N"]:
                break
            print("Please input: Y o N.")

        if option == "Y":
            inventory.clear()
            inventory.update(csv_data)
        else:
            # Actualiza lo existente y agrega lo nuevo sin borrar el resto
            for name, data in csv_data.items():
                inventory[name] = data

        print("\nData successfully loaded.")
        print(f"Invalid rows omitted: {invalid_rows}\n")

    except FileNotFoundError:
        print("File no found.")

                      