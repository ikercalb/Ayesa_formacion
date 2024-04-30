

def get_all_categories():
    #TODO: Completad este método
    #Tiene que devolver un listado con todas las categorias
    #SELECT [attributes] FROM [tablename] WHERE [condition]
    #fetchall() devuelve todos los datos


def find_category_by_id(category_id):
    #TODO: Completad este método
    #Tiene que devolver la categoria que tiene tal id que se pasa por parámetro
    #fetchone() devuelve el primer dato encontrado

def find_category_by_name(category_name):
    #TODO: Completad este método
    #Tiene que devolver la categoria que tiene tal nombre que se pasa por parámetro

#La sentencia para agregar datos a una tabla es:
#INSERT INTO [nombre_de_la_tabla] VALUES (valor1, valor2, valor3,...)
#Los valores deben estar en el orden en el que se declararon en la tabla

print(get_all_categories())
print(find_category_by_id(1))
print(find_category_by_name("dessert"))