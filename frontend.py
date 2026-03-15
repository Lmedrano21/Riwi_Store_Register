import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import backend  # Importamos tu archivo de lógica (backend.py)

# Variable global para llevar la cuenta del total del día
total_del_dia = 0.0

def agregar_venta():
    # Usamos la variable global para poder modificarla
    global total_del_dia 
    
    # 1. RECOLECTAR: Sacamos los textos crudos de las cajas
    nombre_txt = entrada_nombre.get()
    precio_txt = entrada_precio.get()
    cantidad_txt = entrada_cantidad.get()
    
    try:
        # 2. ENVIAR AL BACKEND: Le pasamos los textos a tu función
        # Tu backend se encargará de convertir a float/int y validar
        venta = backend.record_sale(nombre_txt, precio_txt, cantidad_txt)
        
        # 3. SI TODO SALE BIEN: Actualizamos la interfaz
        
        # A) Agregamos la fila a la tabla visual (Treeview)
        tabla_ventas.insert("", "end", values=(
            venta['product'], 
            f"${venta['price']:.2f}", 
            venta['quantity'], 
            f"${venta['total_sale']:.2f}"
        ))
        
        # B) Sumamos al total del día y actualizamos la etiqueta
        total_del_dia += venta['total_sale']
        etiqueta_total_dia.config(text=f"Total del Día: ${total_del_dia:.2f}")
        
        # C) Limpiamos las cajas de texto para la siguiente venta
        entrada_nombre.delete(0, tk.END)
        entrada_precio.delete(0, tk.END)
        entrada_cantidad.delete(0, tk.END)
        
        # Ponemos el cursor (foco) de nuevo en la primera caja
        entrada_nombre.focus()
        
    except ValueError as error:
        # 4. SI EL BACKEND GRITA UN ERROR: Lo atrapamos y mostramos la ventanita
        # 'str(error)' extrae el texto exacto que pusiste en tu backend (ej. "El precio no puede ser negativo")
        messagebox.showwarning("Error de Validación", str(error))

# ==========================================
# CONFIGURACIÓN VISUAL (FRONTEND)
# ==========================================
ventana = tk.Tk()
ventana.title("Sistema de Registro de Ventas")
ventana.geometry("500x550")
ventana.config(padx=20, pady=20)

# --- SECCIÓN 1: FORMULARIO DE ENTRADA ---
marco_formulario = tk.LabelFrame(ventana, text="Nueva Venta", padx=10, pady=10)
marco_formulario.pack(fill="x", pady=(0, 20))

# Nombre
tk.Label(marco_formulario, text="Producto:").grid(row=0, column=0, sticky="w", pady=5)
entrada_nombre = tk.Entry(marco_formulario, width=30)
entrada_nombre.grid(row=0, column=1, pady=5, padx=5)

# Precio
tk.Label(marco_formulario, text="Precio ($):").grid(row=1, column=0, sticky="w", pady=5)
entrada_precio = tk.Entry(marco_formulario, width=30)
entrada_precio.grid(row=1, column=1, pady=5, padx=5)

# Cantidad
tk.Label(marco_formulario, text="Cantidad:").grid(row=2, column=0, sticky="w", pady=5)
entrada_cantidad = tk.Entry(marco_formulario, width=30)
entrada_cantidad.grid(row=2, column=1, pady=5, padx=5)

# Botón Guardar
boton_guardar = tk.Button(marco_formulario, text="Registrar Venta", bg="#4CAF50", fg="white", command=agregar_venta)
boton_guardar.grid(row=3, column=0, columnspan=2, pady=15, ipadx=20)

# --- SECCIÓN 2: HISTORIAL DE VENTAS (LA TABLA) ---
marco_historial = tk.LabelFrame(ventana, text="Historial de Ventas", padx=10, pady=10)
marco_historial.pack(fill="both", expand=True)

# Configuramos las columnas de la tabla (Treeview)
columnas = ("producto", "precio", "cantidad", "total")
tabla_ventas = ttk.Treeview(marco_historial, columns=columnas, show="headings", height=8)

# Definimos los encabezados
tabla_ventas.heading("producto", text="Producto")
tabla_ventas.heading("precio", text="Precio")
tabla_ventas.heading("cantidad", text="Cantidad")
tabla_ventas.heading("total", text="Total")

# Ajustamos el ancho de las columnas
tabla_ventas.column("producto", width=150)
tabla_ventas.column("precio", width=80, anchor="center")
tabla_ventas.column("cantidad", width=80, anchor="center")
tabla_ventas.column("total", width=90, anchor="e")

tabla_ventas.pack(fill="both", expand=True)

# --- SECCIÓN 3: TOTAL DEL DÍA ---
etiqueta_total_dia = tk.Label(ventana, text="Total del Día: $0.00", font=("Arial", 14, "bold"), fg="#D32F2F")
etiqueta_total_dia.pack(pady=15, anchor="e")

# Iniciamos el programa
ventana.mainloop()