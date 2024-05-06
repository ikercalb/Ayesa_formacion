from io import open


def readFileLineByLine(filename):
    #TODO: Completa este método
    #Asigna el fichero a una variable
    fichero = open(filename, 'r')
    #Asigna todas las lineas del fichero a otra variable.
    lines = fichero.readlines()
    #RECUERDA CERRAR EL FICHERO!
    fichero.close()
    #Devuelve ese listado con las lineas del fichero
    return lines

def readFileCompletely(filename):
    #TODO: Completa este método
    #Devuelve todo el texto del archivo en una única variable
    fichero = open(filename, 'r')
    completeFile = fichero.read()
    fichero.close()
    return completeFile




