#Ejercicio24

personas = [("Juan", 25),("María", 30),("Pedro", 40),("Ana", 35),("Luis", 28),("Laura", 22),("Carlos", 33),("Sofía", 29),("Miguel", 45),("Lucía", 27)]
c = 0
for persona, edad in personas:
    if edad >= 40:
        print(persona,edad)
        c += 1
print(c)