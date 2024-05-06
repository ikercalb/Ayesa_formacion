print("Ejercicio 16")

peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / (altura ** 2)

print(imc)

if imc < 18.5:
    print("Peso insuficiente")
elif imc > 18.5 and imc < 24.9:
    print("Peso normal")
elif imc > 25 and imc < 26.9:
    print("Sobrepeso grado 1")
elif imc > 27 and imc < 29.9:
    print("Sobrepeso grado 2")
elif imc > 30 and imc < 34.9:
    print("Obesidad 1")
elif imc > 35 and imc < 39.9:
    print("Obesidad 2")
elif imc > 40 and imc < 49.9:
    print("Obesidad 3 morbida")
elif imc > 50:
    print("Obesidad 4 Extrema")
