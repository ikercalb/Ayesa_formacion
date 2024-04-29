import matplotlib.pyplot as plt

meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
valores = [1,2,3,4,5,6]

plt.plot(meses,valores)
plt.xlabel("xlabel - Meses")
plt.ylabel("ylabel - valores")
plt.title("primer grafico")

#hace un rango desde el 0 hasta el 10
plt.ylim(0,10)
plt.xlim(1,4)

plt.show()