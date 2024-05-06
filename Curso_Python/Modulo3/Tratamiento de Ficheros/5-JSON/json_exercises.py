import json
from io import open


def grow(pet,output):
    #TODO: Incrementamos la edad de la mascota en 1 y la devolvemos
    with open("pets_people.json", "r") as file:
        dictionary_person = json.load(file)
    for person in dictionary_person:
        for pet in person["pets"]:
            pet["age"] += 1


    with open(output, 'w') as file:
        json.dump(dictionary_person, file, indent=4)


#Debemos leer los datos en pets_people.json, incrementar la edad de todas las mascotas y escribirlas de nuevo en un nuevo fichero

input_file = "pets_people.json"
output_file = "pets_people_grown.json"
grow(input_file,output_file)

