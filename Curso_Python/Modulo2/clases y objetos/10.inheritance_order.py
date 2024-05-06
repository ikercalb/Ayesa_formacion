"""
Ejercicio 1.
Heredar la las dos clases Person y Animal en una tercera clase y cuarta clase, cambiando el orden de heredar.
Sobreescribir el metodo move() para imprimir que sois un AnimalPerson o PersonAnimal dependiendo de la clase y
llamar al super() de ese metodo. Comprobar que metodo se ejecuta antes en cada caso.
"""

class Person:

  def move(self):
    print('I am walking')

class Animal:

  def move(self):
    print('I use my legs')

class tercera(Person, Animal):
    def move(self):
        print("AnimalPerson")
        super().move()

class cuarta(Animal, Person):
    def move(self):
        print("PersonAnimal")
        super().move()
       

obj1 = tercera()
obj2 = cuarta()
obj1.move()
obj2.move()