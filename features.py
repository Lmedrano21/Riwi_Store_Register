

def record_sales2(): #This funcition only catch the variables, doesn't make the historial's record sales
    try:    
        print("Sales recorded successfully.")
        record_sales = {}
        producto_name = input("Enter the name of the product: ")
        Producto_price = float(input("Enter the price of the product: "))
        quantity = int(input("Enter the quantity sold: "))

        total_sale = Producto_price * quantity
        record_sales[producto_name] = {
            "price": Producto_price,
            "quantity": quantity,
            "total_sale": total_sale
        }
        return record_sales
    except ValueError:
        print("ERROR: Please enter valid numeric values for price and quantity.")


def record_sales_print():
    validate_record = True
    total_records = {}
    while validate_record:
        decision = input("Do you want to record a sale? (yes/no): ").strip().lower()
        if decision == 'no':
            total_records_day = sum(details['total_sale'] for details in total_records.values())
            print("---------------------------------------------------------")
            print("Thank you for using the sales recording system.")
            print("Here are the recorded sales:")
            for product, details in total_records.items():
                print(f"Product: {product}")
                print(f"  Price: {details['price']}")
                print(f"  Quantity: {details['quantity']}")
                print(f"  Total Sale: {details['total_sale']}")
            print("---------------------------------------------------------")
            print(f"Total sales recorded for the day: {total_records_day}")
            print("---------------------------------------------------------")
            print("Exiting the sales recording system.")
            
            validate_record = False
        elif decision == 'yes':
            total_records.update(record_sales2())
            print("Sales recorded successfully.")
            print("---------------------------------------------------------")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    return