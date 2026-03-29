# Riwi Store Inventory Management System

A comprehensive inventory management system for tech stores. This system allows you to record, manage, update, and analyze product inventory with full data validation and CSV import/export capabilities.

## Features

### Core Functionality
- **Add Products** - Record new products with name, price, and quantity
- **View Inventory** - Display all products in the current inventory
- **Search Products** - Find and display details of specific products
- **Update Products** - Modify product price and/or quantity
- **Delete Products** - Remove products from inventory with confirmation
- **Calculate Statistics** - View inventory analytics including:
  - Total units in stock
  - Total inventory value
  - Most expensive product
  - Product with highest stock level

### Data Management
- **Save to CSV** - Export inventory to CSV file for backup or sharing
- **Load from CSV** - Import products from CSV file with validation
- **Data Validation** - Ensures all inputs are valid:
  - Product names cannot be empty
  - Prices must be positive numbers (greater than zero)
  - Quantities must be positive integers (greater than zero)
- **Error Handling** - User-friendly error messages for invalid inputs

## Requirements

- Python 3.6 or higher
- No external packages required - uses only Python standard library

## Installation

1. Clone the repository
```bash
git clone https://github.com/Lmedrano21/Riwi_Store_Register.git
cd Riwi_Store_Register
```

2. No additional packages required - all dependencies are built-in to Python

## Usage

Run the application:
```bash
python main.py
```

You will see a menu with the following options:
```
1. Add new product      - Add a new item to inventory
2. Print inventory      - View all products in inventory
3. Search a product     - Find details of a specific product
4. Update a product     - Modify product information
5. Delete a product     - Remove a product from inventory
6. Calculate statistics - View inventory analysis and totals
7. Save information in CSV - Export inventory to file
8. Upload information from CSV - Import inventory from file
9. Exit                 - Close the program
```

### Example Workflow
1. Start the program
2. Choose option 1 to add products
3. Enter product name, price, and quantity
4. Choose option 2 to view all products
5. Choose option 6 to see statistics
6. Choose option 7 to save data to CSV before exiting

## Project Structure

- `main.py` - Application entry point that displays welcome message and starts menu
- `menu.py` - Contains the main menu system and user interface
- `features_.py` - Core functions for all inventory operations and validation
- `inventory.csv` - CSV file for storing and loading inventory data
- `new_inventory.csv` - Sample CSV file for importing inventory
- `README.md` - This file

## Input Validation

The system validates all user inputs:
- **Product Names** - Cannot be empty or contain only whitespace
- **Prices** - Must be positive decimal numbers (cannot be zero or negative)
- **Quantities** - Must be positive integers (cannot be zero or negative)

Invalid inputs trigger error messages and prompt the user to try again.

## CSV File Format

When saving or loading inventory via CSV, use the following format:

```
name,price,quantity
Laptop,999.99,5
Mouse,25.50,20
Keyboard,75.00,10
```

The CSV file must have headers in the first row: `name`, `price`, `quantity`

## Author

Lmedrano21
Coder in Riwi