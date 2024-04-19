from os import system

print("Ejercicio 15")

a = input("Primer jugador: pi, pa, ti")
system("cls")
b = input("Segundo jugador: pi, pa, ti")
system("cls")
if  a == "pi" and b == "pi":
         print("empate")
elif a == "pi" and b == "pa":
         print("Gana jugador 2")
elif a == "pi" and b == "ti":
         print("Gana jugador 1")
elif a == "pa" and b == "pi":
         print("Gana jugador 1")
elif a == "pa" and b == "pa":
         print("empate")
elif a == "pa" and b == "ti":
         print("Gana jugador 2")
elif a == "ti" and b == "pi":
         print("Gana jugador 2")
elif a == "ti" and b == "pa":
         print("Gana jugador 1")
elif a == "ti" and b == "ti":
          print("empate")
