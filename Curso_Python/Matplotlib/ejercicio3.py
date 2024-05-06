import matplotlib.pyplot as plt

año2022 = [3000, 3200, 3168, 3111, 3089, 3048, 2992, 2925, 3150, 3200, 2500 , 2500] 
año2023 = [2698, 2745, 2835, 2900, 2971, 2800, 3024, 3113, 3221, 3333, 3300 , 3300]


meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]


plt.plot(meses , año2022)
plt.plot(meses , año2023)

plt.title("gastos 2022-2023")
plt.xlabel("Meses")
plt.ylabel("gastos")
plt.show()

