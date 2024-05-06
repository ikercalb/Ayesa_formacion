"""
Ejercicio final
Crear una clase Pizza

Tendra los siguientes parametros:
  -> Lista de ingredientes: [str]
  -> Tipo de base: str
  -> Tamaño de pizza: int

Debera poder ser creada mediante un constructor, recibiendo todos los parametros indicados anteriormente,
sin limitar el nº de ingredientes.

Debera de tener, ademas, una factoria que permita la creación de pizzas.

Tendra un metodo, "preparar base", que sera privado y que imprimira por pantalla lo siguiente:
  "Extender masa de Y a X cm"
  "Añadir tomate"
  "Añadir queso"

Tendra otro metodo, "hacer pizza", que llamara primero al metodo privado "preparar base" y despues imprimira el resto de ingredientes.

Probar que todo lo anterior funciona.
"""

class Pizza():
  def __init__(self,ingredientes,base,tamaño):
   self.ingredientes = ingredientes
   self.base = base
   self.tamaño = tamaño
   
  def __preparar(self):
    print("externder masa de 0 a ", self.tamaño)
    print("Añadir tomate")
    print("Añadir queso")
  
  def prepararpizza(self):
    self.__preparar()
    for ing in self.ingredientes:
      print('Añadir ',ing)
      
  @classmethod
  def createPizza(cls, ingredientes, base, tamaño):
        return cls(ingredientes, base,tamaño)
   
 
pizza1 = Pizza.createPizza(['bacon','champiñones'], 'Gorda', 30)
print(pizza1.prepararpizza())