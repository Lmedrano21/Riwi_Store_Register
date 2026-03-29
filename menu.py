# Import the inventory dictionary from features_ module
from features_ import inventory
# Import all functions from the features_ module that handle product operations
import features_


# Define the menu function that displays options and handles user choices
def menu():
    # Create a validator variable set to True to keep the menu loop running    
    validator = True
    # Print a line of equals signs for visual separation
    print("=" * 40)
    # Print the menu title
    print("                 Menu")
    # Print another line of equals signs for visual separation
    print("=" * 40)
    # Display option 1: Add new product to inventory
    print("1- Add new product")
    # Display option 2: Show all products in inventory
    print("2- Print inventory")
    # Display option 3: Look for a specific product
    print("3- Search a product")
    # Display option 4: Change product information
    print("4. Update a product")
    # Display option 5: Remove a product from inventory
    print("5- Delete a product")
    # Display option 6: View inventory analysis and totals
    print("6- Calculate statistics")
    # Display option 7: Save inventory to a CSV file
    print("7- Save information in CSV")
    # Display option 8: Load inventory from a CSV file
    print("8- Upload information from CSV")
    # Display option 9: Close the program
    print("9- Exit")
    # Print another line of equals signs for visual separation
    print("=" * 40)
    # Print a blank line for spacing
    print()
    # Start a loop that continues while validator is True
    while validator:
        # Ask user to enter their choice and convert it to an integer
        
        try:
            print("---------------------------------------------------------")
            Ejecucion = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a valid option.")
            continue
        # Check if user chose option 1
        if Ejecucion == 1:
            # Call the add_product function to add a new product
            features_.add_product()
        # Check if user chose option 2
        elif Ejecucion == 2:
            # Call the inventory_print function to display all products
            features_.inventory_print()
        # Check if user chose option 3
        elif Ejecucion == 3:
            # Call the search_producto function to find a specific product
            features_.search_producto()
        # Check if user chose option 4
        elif Ejecucion == 4:
            # Call the product_update function to modify a product
            features_.product_update()
        # Check if user chose option 5
        elif Ejecucion == 5:
            # Call the product_delete function to remove a product
            features_.product_delete()
        # Check if user chose option 6
        elif Ejecucion == 6:
            # Call the calculate_statistics function to show inventory stats
            features_.calculate_statistics()
        # Check if user chose option 7
        elif Ejecucion == 7:
            # Call the save_csv function to save data to a file
            features_.save_csv()
        # Check if user chose option 8
        elif Ejecucion == 8:
            # Call the upload_inventory_csv function to load data from a file
            features_.upload_inventory_csv()
        # Check if user chose option 9
        elif Ejecucion == 9:
            # Print a divider line for visual separation
            print("-----------------------------------------------")
            # Display thank you message to the user
            print("Thanks for using our system! Have a great day!")
            # Print another divider line
            print("-----------------------------------------------")
            # Set validator to False to exit the loop and end the program
            validator =  False
        # Handle case when user enters an invalid option
        else:
            # Let user know their choice was not valid
            print("Option not valid")

