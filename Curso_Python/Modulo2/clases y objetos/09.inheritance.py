"""
Ejercicio 1.
Heredar la clase "Rectangle" en una clase Cube que sobreescriba la funcionalidad del constructor del rectangulo para recibir
el valor de un solo lado y sobreescribir tambien el metodo what_i_am para decir que eres un cubo.

Probarlo despues creando una instancia de Cube.
"""

class Rectangle:

  small_side = 0
  big_side = 0

  def __init__(self, small_side, big_size):
    self.small_side = small_side
    self.big_side = big_size

  def perimeter(self):
    return self.small_side * 2 + self.big_side * 2

  def area(self):
    return self.small_side * self.big_side

  def what_i_am(self):
    print('I am a rectangle')

class cubo(Rectangle):
  def __init__(self, lado):
    super().__init__(lado, lado)
    
  
  def what_i_am(self):
    print('I am a cube')
  
object = cubo(44)

print(object.perimeter())
object.what_i_am()
