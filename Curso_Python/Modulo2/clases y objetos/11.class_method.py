"""
Ejercicio 1.
Vamos a crear una factoria. Crea un metodo de clase que, recibiendo un nombre y una edad, cree personas con esos parametros.
"""

class Person:

  age = 0
  name = ''

  def __init__(self, name, age):
    self.age = age
    self.name = name

  def get_age(self):
    return self.age

  def get_name(self):
    return self.name
  @classmethod
  def create_persona(cls,name,age):
    return Person(name,age)
  
Person1 = Person.create_persona("iker",44)
print(Person1.get_name())
print(Person1.get_age())
