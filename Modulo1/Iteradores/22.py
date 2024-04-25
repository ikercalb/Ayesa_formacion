#Ejercicio22
empleados ={}
while True:
    empleado = input("Introduce el dni del empleado: ")
    sueldo = int(input("Introduce el sueldo del empleado: "))
    
    if 100 <= sueldo <= 1000:
        empleados.update({empleado:sueldo})
    else:
        mayor = []
        menor = []
        suma = 0
        for dni, sueldo in empleados.items(): 
            if sueldo >= 500:
                mayor.append(dni)
            else:
                menor.append(dni)
            suma += sueldo
        print("Mayores de 500 ",len(mayor), "y son", mayor, "menores de 500", len(menor), " y son ", menor)
        print("el total de la empresa es: ", suma)
    