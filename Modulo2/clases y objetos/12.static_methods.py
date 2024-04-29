"""
Ejercicio 1.
Crear un método estatico que, dada una persona, imprima el siguiente texto: "NOMBRE - N AÑOS"
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
  
  @staticmethod
  def imp(name,age):
    print(name," - ", age)
  
  def imp(name, age):
    print(name, "-", age)

Person.imp("manolo", 45)



