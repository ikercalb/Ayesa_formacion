import datetime 
datetimeObject = datetime.datetime.now()

datetimeObject = datetime.date.today()

d = datetime.date(2019,6,6)

d = datetime.date.fromtimestamp(1559811600)

d = datetime.date.fromisoformat('1999-01-01 17:34:45.345')

today = datetime.datetime.time()
print(today.year)

#intervalos de tiempo 
now = datetime.datetime.now()
intervalo = datetime.timedelta(days=5, hours=2)

#ejercicio 8
cumpleaños = datetime(2001,1,28)

timestamp = cumpleaños.timestamp()

