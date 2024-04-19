print("Ejercicio 17")

def suma(a,b):
    return a+b
def resta(a,b): 
    return a-b
def multiplicar(a,b):
    return a*b

operacion = int(input("1 suma 2 resta 3 mutiplicacion"))
a = int(input("Primer valor"))
b = int(input("Segundo valor"))
match operacion:
    case 1:
        print(suma(a,b))
    case 2:
        print(resta(a,b))
    case 3:
        print(multiplicar(a,b))

