import datetime
from dateutil.relativedelta import relativedelta

# datetimeObject = datetime.datetime.now()

# datetimeObject = datetime.date.today()

# d = datetime.date(2019,6,6)

# d = datetime.date.fromtimestamp(1559811600)

# d = datetime.date.fromisoformat('1999-01-01 17:34:45.345')

# today = datetime.datetime.time()
# print(today.year)

# #intervalos de tiempo 
# now = datetime.datetime.now()
# intervalo = datetime.timedelta(days=5, hours=2)

#ejercicio 8

fecha_cumpleaños = input("Introduce tu fecha de cumpleaños (YYYY-MM-DD): ")
cumpleaños = datetime.datetime.strptime(fecha_cumpleaños, "%Y-%m-%d")

print(cumpleaños)

print(datetime.datetime.today()-cumpleaños)

print(cumpleaños.year)

print(cumpleaños.timestamp())

fecha = cumpleaños + relativedelta(month=+1)
print(fecha)
