import csv

list_data = [["first_name", "second_name", "Grade"], ['Alex', 'Brian', 'A'], [
    'Tom', 'Smith', 'B'], ['Jerry', 'Toll', 'A'], ['Erik', 'Bardey', 'B']]

object_data = [{'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'}, {
    'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'},
    {'Grade': 'F', 'first_name': 'Homer', 'last_name': 'Simpson'},
    {'Grade': 'B', 'first_name': 'Jhon', 'last_name': 'Sales'}]


def write_list_csv(list_data, file_path):
    # TODO: Completa este método
    # Debe escribir el listado que se le pasa como parámetro al fichero
    file = open(file_path,'w')
    writer = csv.writer(file)
    writer.writerows(list_data)
    file.close()
    # Si el fichero existe, lo sobreescribe
    # utiliza csv.writer


def write_objects_csv(objects_data, file_path):
    # TODO: Completa este método
    # Debe escribir el listado de diccionarios que se pasa como parámetro al fichero
    # Si el fichero existe, lo sobreescribe
    # utiliza csv.DictWriter
    file = open(file_path, 'w')
    fieldnames = object_data[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(objects_data)


#TODO: Llama a los métodos utilizando las variables correspondientes
write_list_csv(list_data,"data.csv")
write_objects_csv(object_data,"data2.csv")