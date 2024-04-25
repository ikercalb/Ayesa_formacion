a1 = int(input("Primer valor: "))
a2 = int(input("Segundo valor: "))
a3 = int(input("tercer valor: "))


if a1 != a2 and a2 != a3:
    if a2 / a1 == a3 / a2:
        print("sucesion geometrica")
        
    elif a2 - a1 == a3 - a2:
        print("sucesion aritmetica")
        
    else:
        print("sucesion erronea")
        
else:
    print("La sucecion es tanto aritmetica como geometrica")