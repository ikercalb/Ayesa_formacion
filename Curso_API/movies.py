import json
import statistics

with open("movies.json") as file:
    peliculas = json.load(file)

print("## Ejericio 1 ##")
for pelicula in peliculas:
    print("titulo:", pelicula["title"], " año:", pelicula["year"], " duracion:", pelicula["duration"].replace('PT', ''))

print("## Ejericio 2 ##")
for pelicula in peliculas:
    print("titulo:", pelicula["title"], "cantidad de actores:", len(pelicula["actors"]))

print("## Ejericio 3 ##")
p1 = input("introduce una palabra: ").lower()
p2 = input("introduce una palabra: ").lower()
for pelicula in peliculas:
    if p1 in pelicula["storyline"].lower() and p2 in pelicula["storyline"].lower():
        print(pelicula["title"])

print("## Ejericio 4 ##")
actor = input("introduce una palabra: ")
for pelicula in peliculas:
    if actor in pelicula["actors"]:
        print(pelicula["title"])

print("## Ejericio 5 ##")

puntuacion = float(input("introduce una puntuacion: "))
fecha1 = input("introduce una fecha de inicio: YY-mm-dd")
fecha2 = input("introduce una fecha de final: YY-mm-dd")

for pelicula in peliculas:
    if puntuacion < statistics.mean(pelicula["ratings"]) and fecha1 < pelicula["releaseDate"] < fecha2:
        print("Titulo:", pelicula["title"], "Url:", pelicula["posterurl"])
