
def divide(x,y):
    #TODO: Deberá capturar todas las excepciones necesarias, explicando la causa/solución del error en cada caso
    #En caso de que no se produzcan excepciones, mostará el resultado de la división
    #Debe tener una clausa finally que muestre por pantalla: "Limpiando calculadora"
    try:
        result = x / y
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    except TypeError:
        print("No es del tipo indicado")
    else:
        print(result)
    finally:
        print("limpiando calc")
    

#Casos de prueba
divide(2,1)
divide(2,0)
divide("2","1")
print("¡Casos capturados correctamente!")