import math

while True:
    forma = input("T o t para triángulo, C o c para círculo: ")
    
    if forma.lower() == "t":
        print("Triángulo")
        h = int(input("altura: "))
        b = int(input("base: "))
        print((h*b)/2)
        break
    elif forma.lower() == "c":
        print("Círculo")
        r = int(input("radio: "))
        print(math.pi*r**2)
        break
    else:
        print("mal")
        