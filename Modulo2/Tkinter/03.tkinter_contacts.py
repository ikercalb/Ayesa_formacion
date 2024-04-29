import tkinter as tk
from tkinter import messagebox, ttk

# Crear una instancia de Tk
root = tk.Tk()

# Establecer el título y tamaño de la ventana
root.title("Gestion de Contactos")
root.geometry("350x500")

# Crear un Notebook
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Pestaña para agregar contactos
frame_tab1 = ttk.Frame(notebook)
notebook.add(frame_tab1, text="Pestaña 1")

# Etiquetas y entradas para el nombre y teléfono
lab_nombre = tk.Label(frame_tab1, text="Nombre: ")
lab_nombre.grid(row=0, column=0, pady=10)
entrada_nombre = tk.Entry(frame_tab1, width=30)
entrada_nombre.grid(row=0, column=1)

lab_telefono = tk.Label(frame_tab1, text="Telefono: ")
lab_telefono.grid(row=1, column=0, pady=10)
entrada_telefono = tk.Entry(frame_tab1, width=30)
entrada_telefono.grid(row=1, column=1)

# Lista de contactos
contactos = []

# Función para agregar contactos
def agregar_contacto():

    # Recoger el valor del nombre y teléfono    
    nombre = entrada_nombre.get()
    telefono = entrada_telefono.get()
    # Verificar si los campos están llenos
    if nombre and telefono:
    # Agregar el contacto a la lista y limpiar las entradas (entrada_nombre.delete(0, tk.END) y (entrada_telefono.delete(0, tk.END)

    # descomentar estas tres lineas de debajo y la de actualizar_lista_contactos() para terminar esta funcion, 
    # solo hacer la parte de recoger valor y verificar si los campos están llenos
    
        contactos.append((nombre, telefono))
        entrada_nombre.delete(0, tk.END)
        entrada_telefono.delete(0, tk.END)
        actualizar_lista_contactos()
    # Actualizar la lista de contactos
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un artículo.")
    

# CrearBotón para agregar contacto
btn_agregar = tk.Button(frame_tab1, text="Agregar",command=agregar_contacto)
btn_agregar.grid(row=2, column=1)

# Crear Pestaña para visualizar la lista de contactos
frame_tab2 = ttk.Frame(notebook)
notebook.add(frame_tab2, text="Pestaña 2")
# Crear Listbox para mostrar los contactos
listbox_contacto = tk.Listbox(frame_tab2, width=50)
listbox_contacto.grid(row=0, column =1, pady=10, padx=10)
# Función para actualizar la lista de contactos en el Listbox
def actualizar_lista_contactos():

    listbox_contacto.delete(0, tk.END)
    for contacto in contactos:
        listbox_contacto.insert(tk.END, f"{contacto[0]} - {contacto[1]}")



# Función para eliminar el contacto seleccionado
def eliminar_contacto():
    indice = listbox_contacto.curselection()
    if indice:
        listbox_contacto.delete(indice)
        del contactos[indice[0]]
        actualizar_lista_contactos()
    else:
        messagebox.showwarning("Advertencia", "Seleccione un artículo para eliminar.")

# Botón para eliminar contacto
btn_eliminar = tk.Button(frame_tab2, text="Eliminar",command=eliminar_contacto)
btn_eliminar.grid(row=1, column=1, pady=10, padx=10)

# Función para cerrar la aplicación
def cerrar_aplicacion():
    root.quit()

# Crear un menú desplegable
menu_p = tk.Menu(root)
root.config(menu=menu_p)
# Crear un submenú de archivo
submenu = tk.Menu(menu_p, tearoff=0)
# Agregar opción de cerrar aplicación al menú
submenu.add_command(label="cerrar", command=cerrar_aplicacion)
menu_p.add_cascade(label="Archivo", menu=submenu)

# Iniciar el bucle principal
root.mainloop()

