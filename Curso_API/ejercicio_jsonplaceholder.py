import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'
print("##Ejercicio 1##")

response = requests.get(f"{BASE_URL}/posts")
print(response.json())
print(response.status_code)

print("##Ejercicio 2##")

# usuario = input("Introduce el id del usuario: ")
usuario = "101"
new_post = {
    "userId": usuario,
    "id": 101,
    "title": "Holaaa",
    "body": "adioss"
}

response = requests.post(f"{BASE_URL}/posts", json=new_post)
print(response.json())
print(response.status_code)
print("##Ejercicio 3##")

updated_post = {
    "userId": usuario,
    "title": "Hola",
    "body": "adios"
}

response = requests.put(f"{BASE_URL}/posts/100", json=updated_post)
print(response.json())
print(response.status_code)

print("##Ejercicio 4##")

updated_post = {
    "title": "Hola"
}
response = requests.patch(f"{BASE_URL}/posts/100", json=updated_post)
print(response.json())
print(response.status_code)
print("##Ejercicio 5##")

response = requests.delete(f"{BASE_URL}/posts/100")
print(response.json())
print(response.status_code)
print("##Ejercicio 6##")
