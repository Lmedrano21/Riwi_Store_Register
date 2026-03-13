# Riwi Tech Store - Sales Registration System

This project aims o record and manage product sales for a tech store.

## Features

- Record product sales with name, price, and quantity
- Input validation for all product information
- Prevention of invalid data (empty fields, negative values, zero prices)
- User-friendly error messages

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository
```bash
git clone https://github.com/Lmedrano21/Riwi_Store_Register.git
cd Riwi_Tech_Store
```

2. No additional packages required - uses only Python standard library

## Usage

Run the application:
```bash
python main.py
```

Follow the prompts to enter:
- Product name
- Product price
- Quantity sold

The system will validate your input and show error messages if needed.

## Project Structure

- `main.py` - Entry point of the application
- `features.py` - Core functions for sales recording and input validation
- `README.md` - This file

## Error Handling

The application includes validation to ensure:
- Product names are not empty
- Prices are positive numbers (greater than zero)
- Quantities are positive integers (greater than zero)

## Author

Lmedrano21
Coder in Riwi