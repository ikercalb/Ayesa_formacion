from reader import readFileCompletely, readFileLineByLine
#Para testing (No Tocar)
filename = "4. Tratamiento de Ficheros/1-Leyendo_Personas\people.txt"
print("Lectura línea a línea: ")
for l in readFileLineByLine(filename):
    print (l)
print("Lectura completa: ")
print(readFileCompletely(filename))
