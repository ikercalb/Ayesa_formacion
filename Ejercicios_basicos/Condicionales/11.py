print("EJERCICIO 11")

fruta = input("Introcude la fruta: ")
kilos = int(input("Introcude los kilos: "))

frutas = {"manzana": 2.5,"banana": 1.8, "uva": 3.2, "pera": 2.0, "naranja": 2.7 }

if fruta in frutas:
    resultado11 = frutas[fruta]*kilos
    print(resultado11)
else:
    print("No tengo esa fruta")
    