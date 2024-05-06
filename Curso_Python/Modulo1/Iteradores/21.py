#Ejercicio21

tri = {"equilatero": 0 ,"escaleno": 0 ,"isosteles": 0 }

def triangulos(a,b,c):
    if(a==b and a==c):
        print("es equilatero")
        tri["equilatero"] += 1
    elif(a != b and a != c):
        print("es escaleno")
        tri["escaleno"] += 1
    else:
        print("es isosteles")
        tri["isosteles"] += 1


lado1 = input("Introduce el primer lado del triangulo: ") 
lado2 = input("Introduce el segundo lado del triangulo: ")
lado3 = input("Introduce el tercero lado del triangulo: ") 

triangulos(lado1,lado2,lado3)


while True:
    if input("¿Quieres seguir? s/n") == "s":
        
        lado1 = input("Introduce el primer lado del triangulo: ") 
        lado2 = input("Introduce el segundo lado del triangulo: ")
        lado3 = input("Introduce el tercero lado del triangulo: ")
        triangulos(lado1,lado2,lado3)
    else:
        print(tri)
        break
        