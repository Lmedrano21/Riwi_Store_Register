# backend.py

def validate_input_product_name(name):
    # Verificamos que no esté vacío ni lleno de espacios
    if not name or name.strip() == "":
        # 'raise ValueError' es la forma en que el backend "grita" que hubo un error.
        # El frontend escuchará este grito y mostrará el mensaje en la pantalla.
        raise ValueError("El nombre del producto no puede estar vacío.")
    return name.strip()


def validate_input_price(price_input):
    try:
        # Intentamos convertir lo que llegue a flotante
        price = float(price_input)
    except ValueError:
        raise ValueError("Por favor, ingresa un valor numérico válido para el precio.")
    
    # Validamos las reglas de negocio
    if price < 0:
        raise ValueError("El precio no puede ser negativo.")
    if price == 0:
        raise ValueError("El precio no puede ser cero.")
        
    return price


def validate_input_quantity(quantity_input):
    try:
        # Intentamos convertir a entero. Si envían "5.5" o letras, esto fallará.
        quantity = int(quantity_input)
    except ValueError:
        raise ValueError("La cantidad debe ser un número entero válido (sin decimales ni letras).")
    
    if quantity < 0:
        raise ValueError("La cantidad no puede ser negativa.")
    if quantity == 0:
        raise ValueError("La cantidad no puede ser cero.")
        
    return quantity


def record_sale(name_input, price_input, quantity_input):
    """
    Esta es la función principal de tu backend.
    Recibe los datos crudos del frontend, los valida usando las funciones de arriba,
    calcula el total y devuelve el registro de la venta.
    """
    # 1. Validamos todos los datos de entrada
    valid_name = validate_input_product_name(name_input)
    valid_price = validate_input_price(price_input)
    valid_quantity = validate_input_quantity(quantity_input)

    # 2. Hacemos el cálculo
    total_sale = valid_price * valid_quantity
    
    # 3. Empaquetamos y devolvemos el resultado
    return {
        "product": valid_name,
        "price": valid_price,
        "quantity": valid_quantity,
        "total_sale": total_sale
    }