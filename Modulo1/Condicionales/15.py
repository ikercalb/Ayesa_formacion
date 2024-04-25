from os import system

print("Ejercicio 15")

primero = input("Primer jugador: pi, pa, ti")
system("cls")
segundo = input("Segundo jugador: pi, pa, ti")
system("cls")

if  primero == "pi" and segundo == "pi":
         print("empate")
         
elif primero == "pi" and segundo == "pa":
         print("Gana jugador 2")
         
elif primero == "pi" and segundo == "ti":
         print("Gana jugador 1")
         
elif primero == "pa" and segundo == "pi":
         print("Gana jugador 1")
         
elif primero == "pa" and segundo == "pa":
         print("empate")
         
elif primero == "pa" and segundo == "ti":
         print("Gana jugador 2")
         
elif primero == "ti" and segundo == "pi":
         print("Gana jugador 2")
         
elif primero == "ti" and segundo == "pa":
         print("Gana jugador 1")
         
elif primero == "ti" and segundo == "ti":
          print("empate")
