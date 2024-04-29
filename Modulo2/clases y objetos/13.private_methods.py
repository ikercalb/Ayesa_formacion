"""
Ejercicio 1.
Crear un metodo privado, 'increment_age(n)' en la clase Person que incremente la edad de la persona en el numero de años dado.
Crear un segundo metodo, 'happy_birthday()' no privado que sume un año usando el metodo anterior.

Crear un objeto Person, llamar a happy_birthday y comprobar que la edad se ha incrementado en 1.
Probar a llamar al metodo increment_age y ver como falla la llamada.
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
  
  def __increment_age(self, n):
    n+=1
    return n
  
  def happy_birthday(self):
    return self.__increment_age(self.age)

obj = Person("manolo", 33)

print(obj.happy_birthday())





  
  
 
