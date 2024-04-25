print("Ejercicio 17")

def suma(a,b):
    return a+b
def resta(a,b): 
    return a-b
def multiplicar(a,b):
    return a*b
def division(a,b):
    return a/b

operacion = int(input("1 para suma 2 para resta 3 para mutiplicacion 4 para division"))
a = int(input("Primer valor"))
b = int(input("Segundo valor"))   
match operacion:
    case 1:
        print(suma(a,b))
    case 2:
        print(resta(a,b))
    case 3:
        print(multiplicar(a,b))
    case 4:
        print(division(a,b))
















