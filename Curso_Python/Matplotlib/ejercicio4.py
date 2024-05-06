import matplotlib.pyplot as plt

Motoburguer=[6.5, 7.2, 7.3, 7.1, 7.5, 5.3, 6.2] 
Perritravel = [8.0, 7.5, 7.2, 6.3, 6.0, 5.0, 5.5] 
Iberfood = [5.3, 6.8, 7.0, 6.5, 7.8, 8.0, 7.5]
dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

plt.plot(dias, Motoburguer, color= 'green', marker = "*",label= "Motoburguer")
plt.plot(dias, Perritravel, color= "#0000d0", marker = "p",label= "Perritravel")
plt.plot(dias, Iberfood, color=(194/255, 40/255, 29/255), marker = "s",label= "Iberfood")

plt.title("Concurso foodtruck")
plt.xlabel("Dias de la semana")
plt.ylabel("Medias de valoracion")

plt.ylim(0,7)
plt.ylim(0,10)

plt.legend(loc = 'lower left')


plt.show()
