#Grafica2
import matplotlib.pyplot as plt
ids = [1,2,3,4,5]
sueldos = [500,550,1000,1100,600]

while True:

        id = input("introduce el id de trabajador")
        sueldo = int(input("introduce el salario"))
        if sueldo >= 500 and sueldo <= 1500:
            ids.append(id)
            sueldos.append(sueldo)
        else:
            print("sueldo incorrecto")
            
        c = input("Desea seguir s/n")
        if c == "n" and len(ids) >= 5:
            break
 
plt.plot(ids,sueldos)
plt.xlabel("ids")
plt.ylabel("Sueldo")
plt.title("ejercicio2")

plt.ylim(500,1500)


plt.show()