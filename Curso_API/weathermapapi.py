import requests


KEY = "f448c91c13e9f12fe012b9d97ec2fd30"

ciudad = input("Nombre de la ciudad: ")

BASE_URL = 'http://api.openweathermap.org/data/2.5'

response = requests.get(f"{BASE_URL}/weather?q={ciudad}&appid={KEY}")
r = response.json()
tem = r['main']['temp']
desc = r['weather'][0]['description']
tem = tem-273.15


print(tem, desc)