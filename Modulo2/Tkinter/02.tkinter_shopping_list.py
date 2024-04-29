import tkinter as tk
from tkinter import messagebox, ttk

# Crear una instancia de Tk
root = tk.Tk()

# Establecer el título de la ventana
root.title("Lista de Compras")

# Crear widgets de la interfaz

# 1) Label "Ingrese un artículo:"
lab_articulo = tk.Label(root,text="Ingrese un artículo: ", font=("Arial",8))
lab_articulo.grid(row=0, column=0, pady=10)

# 2) Entry para ingresar un artículo
entrada_articulo = tk.Entry(root, font=("Arial",8))
entrada_articulo.grid(row=0, column=1, pady=10, padx=10)
# 3) Listbox para mostrar la lista de compras
listbox_compras = tk.Listbox(root, width=30)
listbox_compras.grid(row=1, column =1, pady=10)
# Botones de control



################################################################################################
# ¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡A partir de esta línea, no tocar las funciones!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
################################################################################################

# Función para agregar un artículo a la lista
def agregar_articulo():
    articulo = entrada_articulo.get()
    # En este caso, el artículo es el texto que hemos introducido en el output, 
    # el get() método se utiliza para obtener el texto de la entrada
    if articulo:
        listbox_compras.insert(tk.END, articulo)
        # En un listbox con insert, tk.END es el índice especial que representa el final de la lista
        #(define que el elemento que añadamos se ira al final de la lista)
        entrada_articulo.delete(0, tk.END)
        # En el caso de un Entry con delete, tk.END representa el final del texto. 
        # (limpiamos el contenido de la barra del input (Entry))
    else:
        # En caso de que no se haya introducido nada en el input, se muestra un mensaje de advertencia
        messagebox.showwarning("Advertencia", "Por favor, ingrese un artículo.")

# Función para eliminar un artículo de la lista
def eliminar_articulo():
    indice = listbox_compras.curselection()
    if indice:
        listbox_compras.delete(indice)
    else:
        messagebox.showwarning("Advertencia", "Seleccione un artículo para eliminar.")


# 1) Botón "Agregar"
btn_agregar = tk.Button(root,text="Agregar",command=agregar_articulo)
btn_agregar.grid(row=2, column=0, pady=10, padx=10)
# 2) Botón "Eliminar"
btn_eliminar = tk.Button(root, text="Eliminar",command=eliminar_articulo)
btn_eliminar.grid(row=2, column=3, pady=10, padx=10)


# Iniciar el bucle principal
root.mainloop()
