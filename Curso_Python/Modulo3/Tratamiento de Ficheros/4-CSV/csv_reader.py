import csv

def read_all_people(file_path):
    #TODO Completar este método
    #Teneis que devolver todas las líneas que aparecen en el fichero CSV
    #Usa csv.reader()
    file = open(file_path,encoding="UTF-8")
    reader = csv.reader(file)
    all_people = []
    next(reader)
    for row in reader:
        all_people.append(row)
    return all_people

def read_only_names(file_path):
    #TODO Completar este método
    #Debéis obtener únicamente el listado de nombres
    #Usa csv.DictReader()
    file = open(file_path,encoding="UTF-8")
    reader = csv.DictReader(file)
    only_names = []
    for row in reader:
        only_names.append(row['name'])
    return only_names


#TESTING No tocar
file_path = "people.csv"
print("Listado de todas las personas: ")
print(read_all_people(file_path))
print("Listado de únicamente los nombres: ")
print(read_only_names(file_path))