import requests
import tkinter as tk
from tkinter import ttk, messagebox

# Función para obtener las tasas de cambio desde la API
def obtener_tasas():
    url = "https://api.exchangerate-api.com/v4/latest/USD"  # URL de la API
    response = requests.get(url)  # Hacemos la solicitud
    if response.status_code == 200:  # Si la solicitud fue exitosa
        return response.json()["rates"]  # Retornamos las tasas de cambio
    else:
        messagebox.showerror("Error", "No se pudieron obtener las tasas de cambio.")
        return None

# Función para convertir la moneda
def convertir():
    try:
        cantidad = float(entry_cantidad.get())  # Tomamos la cantidad ingresada
        moneda_origen = combo_moneda_origen.get()  # Moneda de origen seleccionada
        moneda_destino = combo_moneda_destino.get()  # Moneda destino seleccionada
        
        # Calculamos la tasa de conversión
        tasa = tasas[moneda_destino] / tasas[moneda_origen]
        resultado = cantidad * tasa  # Convertimos la cantidad
        label_resultado.config(text=f"{cantidad} {moneda_origen} = {resultado:.2f} {moneda_destino}")  # Mostramos el resultado
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una cantidad válida.")  # Si la cantidad es inválida

# Interfaz gráfica con Tkinter
ventana = tk.Tk()
ventana.title("Conversor de Monedas")
ventana.geometry("300x250")

# Obtener las tasas de cambio desde la API
tasas = obtener_tasas()
monedas = list(tasas.keys()) if tasas else []  # Listamos las monedas disponibles

# Elementos de la interfaz gráfica
label_cantidad = tk.Label(ventana, text="Cantidad:")
label_cantidad.pack()

entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack()

label_origen = tk.Label(ventana, text="Moneda de origen:")
label_origen.pack()

combo_moneda_origen = ttk.Combobox(ventana, values=monedas)
combo_moneda_origen.pack()

label_destino = tk.Label(ventana, text="Moneda de destino:")
label_destino.pack()

combo_moneda_destino = ttk.Combobox(ventana, values=monedas)
combo_moneda_destino.pack()

# Botón para realizar la conversión
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.pack()

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.pack()

# Ejecutar la ventana de la aplicación
ventana.mainloop()
