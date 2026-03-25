import features_


import csv

inventory = features_.add_product()

# CSV file name
csv_filename = "inventory.csv"

# Define the field names (headers)
fieldnames = ["name", "price", "quantity"]

# Writing to CSV
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Write header row
    writer.writerow(inventory)  # Write data rows
    

with open('inventory.csv', mode ='r') as file:    
       csvFile = csv.DictReader(file)
       for lines in csvFile:
            print(lines)
