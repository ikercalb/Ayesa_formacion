import math

forma = input("T o t para triángulo, C o c para círculo: ")
    
if forma.lower() == "t":
    print("Triángulo")
    h = int(input("altura: "))
    b = int(input("base: "))
    print((h*b)/2)
    
elif forma.lower() == "c":
    print("Círculo")
    r = int(input("radio: "))
    print(math.pi*r**2)
    
else:
    print("Introducido mal valor")
        