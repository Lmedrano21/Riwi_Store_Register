# Import the csv module to read and write CSV files
import csv
# Import the os module to work with file paths and check if files exist
import os

# Declare global variables that will be accessible throughout the entire module
# Create a global inventory dictionary to store all products
global inventory, inventory_for_csv, inventory_from_csv
# Initialize inventory as an empty dictionary to hold product data
inventory = {}
# Initialize a list to temporarily hold products before saving to CSV file
inventory_for_csv = []
# Initialize a dictionary to store products loaded from a CSV file
inventory_from_csv = {}
# Initialize a dictionary to track products that were added (not currently used)
products_added = {}

# Define a function to validate that a product name is not empty
def validate_input_product_name(user_input):
    # Start a loop that continues while the input is empty
    while user_input.strip() == "":
        # Tell user that product name cannot be empty
        print("ERROR: Product name cannot be empty. Please enter a valid product name.")
        # Ask user to enter the product name again
        user_input = input("Enter the name of the product: ")
    # Return the product name after removing extra whitespace
    return user_input.strip()

# Define a function to validate that a product price is a valid positive number
def validate_input_price(user_input):
    # Create a variable to control the validation loop
    validate = True
    # Start an infinite loop for validation
    while True:
        # Try to convert the input to a decimal number
        try:
            # Convert user input to a floating point number
            price = float(user_input)
            # Check if the price is negative
            if price < 0:
                # Tell user that price cannot be negative
                print("ERROR: Price cannot be negative. Please enter a valid price.")
                # Ask user to try again
                user_input = input("Enter the price of the product: ")
            # Check if the price is exactly zero
            elif price == 0:
                # Tell user that price cannot be zero
                print("ERROR: Price cannot be zero. Please enter a valid price.")
                # Ask user to try again
                user_input = input("Enter the price of the product: ")
            # Check if the price is empty (this condition is not needed after float conversion)
            elif price == "":
                # Tell user that price cannot be empty
                print("ERROR: Price cannot be empty. Please enter a valid price.")
                # Ask user to try again
                user_input = input("Enter the price of the product: ")
            # If price is valid
            else:
                # Set validate to False to exit the loop
                validate = False
                # Return the valid price
                return price
        # Handle case where user enters text instead of a number
        except ValueError:
            # Tell user that they must enter a number
            print("ERROR: Please enter a valid numeric value for price.")
            # Ask user to try again
            user_input = input("Enter the price of the product: ")

# Define a function to validate that a product quantity is a valid positive integer
def validate_input_quantity(user_input):
    # Create a variable to control the validation loop
    validate = True
    # Start an infinite loop for validation
    while validate:
        # Try to convert the input to a whole number
        try:
            # Convert user input to an integer
            quantity = int(user_input)
            # Check if the quantity is negative
            if quantity < 0:
                # Tell user that quantity cannot be negative
                print("ERROR: Quantity cannot be negative. Please enter a valid quantity.")
                # Ask user to try again
                user_input = input("Enter the quantity sold: ")
            # Check if the quantity is exactly zero
            elif quantity == 0:
                # Tell user that quantity cannot be zero
                print("ERROR: Quantity cannot be zero. Please enter a valid quantity.")
                # Ask user to try again
                user_input = input("Enter the quantity sold: ")
            # Check if the quantity is empty
            elif quantity == "":
                # Tell user that quantity cannot be empty
                print("ERROR: Quantity cannot be empty. Please enter a valid quantity.")
                # Ask user to try again
                user_input = input("Enter the quantity sold: ")
            # Check if the quantity is None (no value)
            elif quantity is type(None):
                # Tell user that quantity cannot be None
                print("ERROR: Quantity cannot be None. Please enter a valid quantity.")
                # Ask user to try again
                user_input = input("Enter the quantity sold: ")
            # Check if the quantity is a decimal number instead of an integer
            elif quantity == type(float):
                # Tell user that quantity must be a whole number
                print("ERROR: Quantity must be an integer. Please enter a valid quantity.")
                # Ask user to try again
                user_input = input("Enter the quantity sold: ")
            # If quantity is valid
            else:
                # Set validate to False to exit the loop
                validate = False
                # Return the valid quantity
                return quantity
        # Handle case where user enters text instead of a number
        except ValueError:
            # Tell user that they must enter a number
            print("ERROR: Please enter a valid numeric value for quantity.")
            # Ask user to try again
            user_input = input("Enter the quantity sold: ")

# Define the function to add a new product to the inventory
def add_product():
    # Create an empty dictionary to hold the new product
    product_added_to_saved = {}
    # Use try-except to handle any errors during input
    try:
        # Ask user to enter the product name
        producto_name = input("Enter the name of the product: ")
        # Validate the product name to ensure it is not empty
        producto_name = validate_input_product_name(producto_name)
        # Ask user to enter the product price
        Producto_price = input("Enter the price of the product: ")
        # Validate the product price to ensure it is valid
        Producto_price = validate_input_price(Producto_price)
        # Ask user to enter the product quantity
        quantity = input("Enter the quantity: ")
        # Validate the quantity to ensure it is valid
        quantity = validate_input_quantity(quantity)
        
        # Add the product to a temporary dictionary with product name as the key
        product_added_to_saved[producto_name] = {
            # Store the product name
            "name": producto_name,
            # Store the product price
            "price": Producto_price,
            # Store the product quantity
            "quantity": quantity,
        }
        # Add the new product to the main inventory dictionary
        inventory.update(product_added_to_saved)
        
        # Create another dictionary with the same product info for CSV saving
        product_added_to_saved_csv = {
            # Store the product name
            "name": producto_name,
            # Store the product price
            "price": Producto_price,
            # Store the product quantity
            "quantity": quantity,
        }
        
        # Add the product to the list that will be saved to CSV
        inventory_for_csv.append(product_added_to_saved_csv)
        # Display the current list of items to be saved (for debugging)
        for key, product in product_added_to_saved.items():
            print("---------------------------------------------------------")
            print(f"Product to save: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
        # Tell user that the product was added successfully
        print("Product added successfully")
        print("---------------------------------------------------------")
        # Exit the function
        return
    # Handle any value errors if invalid data is entered
    except ValueError:
        # Tell user that price and quantity must be valid numbers
        print("ERROR: Please enter valid numeric values for price and quantity.")

# Define the function to save all products to a CSV file
def save_csv():
    # Set the filename where data will be saved
    csv_filename = "inventory.csv"
    # Create a list of column names for the CSV file
    fieldnames = ["name", "price", "quantity"]
    # Use try-except to handle file writing errors
    try:
        # Check if the CSV file exists and is not empty
        file_exists = os.path.isfile(csv_filename) and os.path.getsize(csv_filename) > 0
        
        # Open the CSV file in append mode (add data to the end)
        with open(csv_filename, mode='a', newline='', encoding='utf-8') as file:
            # Create a CSV writer that will write dictionaries as rows
            writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction='ignore')
            
            # If the file is new, write the column headers
            if not file_exists:
                # Write the header row with column names
                writer.writeheader()
            # Write all the products from inventory_for_csv list to the file
            writer.writerows(inventory_for_csv)
            
        # Tell user that the file was saved successfully
        print("CSV file is saved successfully")
        # Clear the list since data has been saved
        inventory_for_csv.clear()
        
    # Handle any errors that occur during file writing
    except Exception as e:
        # Display the error message to the user
        print(f"Error saving CSV: {e}")

# Define the function to display all products currently in inventory
def inventory_print():
    # Create an empty dictionary for displaying inventory
    total_records = {}
    # Copy all products from inventory into total_records
    total_records.update(inventory)
    # Print a divider line for visual separation
    print("---------------------------------------------------------")
    # Print a header message
    print("Here are your inventory")
    # Loop through each product in the inventory
    for product, details in total_records.items():
        # Print the product name
        print(f"Product: {product}")
        # Print the product price with indentation
        print(f"  Price: {details['price']}")
        # Print the product quantity with indentation
        print(f"  Quantity: {details['quantity']}")
    # Print a divider line for visual separation
    print("---------------------------------------------------------")

    return

# Define the function to search for a specific product in inventory
def search_producto():
    # Ask user to enter the name of the product they want to find
    name_to_search = input("Please input the name's product to search: ")

    # Try to find the product in the inventory dictionary
    producto_info = inventory.get(name_to_search)
    # Check if the product was found
    if producto_info:
        # Print a header for the product information
        print(f"Information: ")
        # Print the product name
        print(f"Name: {producto_info['name']}")
        # Print the product price
        print(f"Price: {producto_info['price']}")
        # Print the product quantity
        print(f"Quantity: {producto_info['quantity']}")
        # Print a divider line
        print("---------------------------------------------------------")
    # If product was not found
    else:
        # Tell user that the product does not exist
        print(f"The product '{name_to_search}' is not found, please try again.")
        # Print a divider line
        print("---------------------------------------------------------")

# Define the function to calculate and display inventory statistics
def calculate_statistics():
    # Create an empty dictionary to work with inventory data
    product_added = {}
    # Copy all products from the main inventory into this dictionary
    product_added.update(inventory)

    # Check if there are no products in the inventory
    if not product_added:
        # Tell user that inventory is empty
        print("\n The inventory is empty.")
        # Exit the function early
        return

    # Define a lambda function to calculate total value of a product (price × quantity)
    # A lambda is a quick way to create a simple function
    calculate_subtotal = lambda d: d['price'] * d['quantity']

    # Calculate the total number of units across all products
    # Use a sum with generator expression to add up all quantities
    total_units = sum(d['quantity'] for d in product_added.values())
    # Calculate the total value of all products
    # Use a sum to add up the subtotal (price × quantity) for each product
    total_value = sum(calculate_subtotal(d) for d in product_added.values())

    # Find the product with the highest price
    # The max() function with a lambda key function finds the maximum based on price
    expensive_name, expensive_data = max(product_added.items(), key=lambda item: item[1]['price'])
    # Find the product with the highest quantity in stock
    # The max() function finds the maximum based on quantity
    stock_name, stock_data = max(product_added.items(), key=lambda item: item[1]['quantity'])

    # Print a blank line for spacing
    print("\n---------------------------------------------------------")
    # Print a header for the statistics section
    print("                INVENTORY STATISTICS")
    # Print a divider line
    print("---------------------------------------------------------")
    # Print the total number of units in inventory
    print(f"Total units:          {total_units}")
    # Print the total value of all inventory in dollars
    print(f"Total value:          ${total_value:,.2f}")
    # Print the name and price of the most expensive product
    print(f"Most expensive:       {expensive_name} (${expensive_data['price']})")
    # Print the name and quantity of the product with most stock
    print(f"Highest stock:        {stock_name} ({stock_data['quantity']} units)")
    # Print a divider line
    print("---------------------------------------------------------")
    # Exit the function
    return

# Define the function to update an existing product in inventory
def product_update():
    # Ask user to enter the name of the product they want to update
    name_to_search = input("Please input the name's product to update: ")

    # Try to find the product in the inventory dictionary
    producto_info = inventory.get(name_to_search)
    
    # Check if the product was not found
    if not producto_info:
        # Tell user that the product was not found
        print(f" Product '{producto_info['name']}' not found.")
        # Exit the function
        return
    
    # Print current product information
    print(f"\nUpdate: {producto_info['name']} (Price: {producto_info['price']}, Stock: {producto_info['quantity']})")
    # Print option 1 to change only the price
    print("1. Change Price")
    # Print option 2 to change only the stock quantity
    print("2. Change Stock")
    # Print option 3 to change both price and stock
    print("3. Change Both")
    
    # Ask user which update option they want to choose
    option = input("Choose an option: ")

    # Check if user chose option 1
    if option == "1":
        # Ask for new price and update it
        producto_info["price"] = float(input("New price: "))
    # Check if user chose option 2
    elif option == "2":
        # Ask for new stock quantity and update it
        producto_info["quantity"] = int(input("New stock: "))
    # Check if user chose option 3
    elif option == "3":
        # Ask for new price and update it
        producto_info["price"] = float(input("New price: "))
        # Ask for new stock quantity and update it
        producto_info["quantity"] = int(input("New stock: "))
    # Handle invalid option
    else:
        # Tell user they selected an invalid option
        print("Invalid option.")
        
    # Tell user that the update was successful
    print(" Update successful.")
    # Exit the function
    return

# Define the function to delete a product from inventory
def product_delete():
    # Ask user to enter the name of the product they want to delete
    name = input("Enter the name of the product you wish to delete: ")
    # Check if the product exists in the inventory
    if name in inventory:
        # Ask user to confirm they want to delete the product
        confirmar = input(f" Are you sure you want to delete '{name}'? (Yes/No): ").lower()
        
        # Check if user confirmed by typing 'yes'
        if confirmar == 'yes':
            # Remove the product from the inventory dictionary
            del inventory[name]
            # Tell user that the product was deleted successfully
            print(f" The product '{name}' has been successfully deleted.")
            # Exit the function
            return
        # If user did not confirm
        else:
            # Tell user that the operation was cancelled
            print(" Operation cancelled by the user")
            # Exit the function
            return
    # If the product does not exist in inventory
    else:
        # Tell user that the product was not found
        print(f" Error: The product '{name}' does not exist in the inventory.")
        # Exit the function
        return


# Define the function to load products from a CSV file
def upload_inventory_csv(route="new_inventory.csv"):
    # Create a counter variable to track invalid rows
    invalid_rows = 0
    # Create a temporary dictionary to store CSV data
    csv_data = {}
    
    # Use try-except to handle file reading errors
    try:
        # Open the CSV file in read mode with UTF-8 encoding
        with open(route, 'r', encoding='utf-8') as csvfile:
            # Create a CSV reader object
            result = csv.reader(csvfile)
            # Try to get the header row (first row of the file)
            try:
                # Read the first row as the header
                header = next(result)
            # Handle case where file is empty
            except StopIteration:
                # Tell user that the file is empty
                print("The file is empty.")
                # Exit the function
                return

            # Convert header text to lowercase and remove extra spaces
            header = [h.strip().lower() for h in header]
            # Check if the header matches the expected format
            if header != ['name', 'price', 'quantity']:
                # Tell user that the header format is wrong
                print("The CSV header is invalid. Expected: name, price, quantity")
                # Exit the function
                return

            # Loop through each row in the CSV file (skip header)
            for fila in result:
                # Check if the row has exactly 3 columns and all have data
                if len(fila) == 3 and all(item.strip() for item in fila):
                    # Try to convert the row data to correct formats
                    try:
                        # Get the product name from the first column
                        name = fila[0].strip()
                        # Convert the price from string to decimal number
                        price = float(fila[1])
                        # Convert the quantity from string to whole number
                        quantity = int(fila[2])

                        # Check if price and quantity are positive values
                        if price > 0 and quantity > 0:
                            # Store the product data in the temporary dictionary
                            csv_data[name] = {'name': name, 'price': price, 'quantity': quantity}
                        # If values are not positive
                        else:
                            # Increment the invalid rows counter
                            invalid_rows += 1
                    # Handle conversion errors (text instead of numbers)
                    except ValueError:
                        # Increment the invalid rows counter
                        invalid_rows += 1
                # If row does not have exactly 3 columns or is empty
                else:
                    # Increment the invalid rows counter
                    invalid_rows += 1
                    
        # Check if any valid data was found in the CSV
        if not csv_data:
            # Tell user that no valid data was loaded
            print("No valid data was found to load.")
            # Exit the function
            return

        # Loop until user gives a valid yes/no answer
        while True:
            # Ask user if they want to replace all current inventory with CSV data
            option = input("\nDo you want to overwrite the entire current inventory? (Y/N): ").strip().upper()
            # Check if user entered Y or N
            if option in ["Y", "N"]:
                # Exit the input loop
                break
            # If user entered something else
            print("Please input: Y or N.")

        # Check if user chose to overwrite (Y)
        if option == "Y":
            # Remove all products from current inventory
            inventory.clear()
            # Clear the list of products to save
            inventory_for_csv.clear()
            
            # Add each product from CSV data to inventory
            for name, data in csv_data.items():
                # Add the product to the main inventory
                inventory[name] = data
                # Add the product to the save list
                inventory_for_csv.append(data)
        # If user chose not to overwrite (N)
        else:
            # Loop through each product from the CSV data
            for name, data in csv_data.items():
                # Update the existing product or add new product to inventory
                inventory[name] = data
                # Clear the save list
                inventory_for_csv.clear()
                # Rebuild the save list from the updated inventory
                inventory_for_csv.extend(inventory.values())

        # Tell user that data was loaded successfully
        print("\nData successfully loaded.")
        # Tell user how many rows had errors and were skipped
        print(f"Invalid rows omitted: {invalid_rows}\n")

    # Handle case where the CSV file is not found
    except FileNotFoundError:
        # Tell user that the file does not exist
        print("File not found.")