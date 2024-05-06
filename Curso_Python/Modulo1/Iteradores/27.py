#Ejercicio27
num = int(input("introduce un numero inferior a 100"))
res = 0
cadena = 'puedo aprobar es'
print(cadena[7:13])
if 0 < num < 100:
   for i in range(num,100,5):
       res += i**2
else:
    print("numero erroneo")
    
print(res)