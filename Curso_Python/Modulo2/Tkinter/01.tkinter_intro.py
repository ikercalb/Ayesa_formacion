import tkinter as tk

# Crear una instancia de Tk
root = tk.Tk()

# Establecer el título de la ventana
root.title("Formulario de Registro")
# Establecer el tamaño de la ventana (ancho, alto)
root.geometry("450x500")


# Crear las etiquetas y cuadros de entrada para nombre (entrada_nombre) y edad (entrada_edad)
lab_nombre = tk.Label(root,text="Nombre: ", font=("Arial",8))
lab_nombre.grid(row=0, column=0, pady=10)
lab_edad = tk.Label(root,text="Edad: ", font=("Arial",8))
lab_edad.grid(row=1, column=0, pady=10)

entrada_nombre = tk.Entry(root, width=30)
entrada_nombre.grid(row=0, column=1)
entrada_edad = tk.Entry(root, width=30)
entrada_edad.grid(row=1, column=1)

# Crear una etiqueta y radiobuttons (radio_femenino, radio_masculino) para el género 
lab_genero = tk.Label(root,text="Género: ", font=("Arial",8))
lab_genero.grid(row=2, column=0,)
genero = tk.IntVar()
radio_femenino = tk.Radiobutton(root,text="Femenino", variable=genero, value=1)
radio_femenino.grid(row=2, column=1)
radio_masculino = tk.Radiobutton(root,text="Masculino", variable=genero, value=2)
radio_masculino.grid(row=2, column=2)

# Crear una etiqueta y checkbuttons (check_email, check_telefono) para preferencias de contacto
entrada_pref = tk.Label(root,text="Preferencias de contacto: ", font=("Arial",8))
entrada_pref.grid(row=3, column=0)
email_var = tk.BooleanVar()
tel_var = tk.BooleanVar()
check_email = tk.Checkbutton(root,text="Email", variable=tel_var)
check_email.grid(row=3, column=1)
check_telefono = tk.Checkbutton(root,text="Telefono", variable=email_var)
check_telefono.grid(row=3, column=2)

################################################################################################
# ¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡A partir de esta línea, no tocar las funciones!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
################################################################################################

# Crear una caja de texto (Text) para mostrar la información de los usuarios registrados
caja_texto = tk.Text(root, width=50, height=5)
caja_texto.grid(row=4, column=0, columnspan=3, padx=10, pady=10)


# Función para verificar si los campos requeridos están completos
def verificar_campos():
    if entrada_nombre.get() and entrada_edad.get():
        boton_enviar.config(state=tk.NORMAL)
    else:
        boton_enviar.config(state=tk.DISABLED)

# Asociar la verificación de campos a los eventos de entrada
entrada_nombre.bind("<KeyRelease>", lambda event: verificar_campos())
entrada_edad.bind("<KeyRelease>", lambda event: verificar_campos())

# Función para enviar el formulario e imprimir la información en la caja de texto
def enviar_formulario():
    # Obtener los valores de las entradas
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    genero_seleccionado = genero.get()
    
    # Obtener las preferencias de contacto seleccionadas
    preferencias_contacto = []
    if check_email.get():
        preferencias_contacto.append("Email")
    if check_telefono.get():
        preferencias_contacto.append("Teléfono")
    
    # Crear una línea con la información ingresada
    informacion_usuario = f"Nombre: {nombre}, Edad: {edad}, Género: {genero_seleccionado}, Preferencias: {', '.join(preferencias_contacto)}\n"
    
    # Imprimir la información en la caja de texto
    caja_texto.insert(tk.END, informacion_usuario)
    
    # Limpiar los campos de entrada
    entrada_nombre.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)
    genero.set("Femenino")
    check_email.deselect()
    check_telefono.deselect()
    
    # Deshabilitar el botón de enviar hasta que los campos estén completos
    boton_enviar.config(state=tk.DISABLED)

# Función para limpiar la caja de texto
def reset_caja_texto():
    caja_texto.delete("1.0", tk.END)

# Crear un botón para enviar el formulario
boton_enviar = tk.Button(root, text="Enviar formulario", command=enviar_formulario, state=tk.DISABLED)
boton_enviar.grid(row=5, column=1, columnspan=2, pady=10)

# Crear un botón para resetear la caja de texto
boton_reset = tk.Button(root, text="Resetear caja de texto", command=reset_caja_texto)
boton_reset.grid(row=5, column=0, pady=10)

# Iniciar el bucle principal
root.mainloop()
