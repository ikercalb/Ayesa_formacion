"""
Ejercicio 1.
Heredar la clase "Rectangle" en otra clase a vuestra elección y comprobar como podeis llamar a los mismos métodos que
tiene la clase Rectangle.
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

class trapecio(Rectangle):
    def __init__(self, small_side, big_size):
      super().__init__(small_side, big_size)

obj = trapecio(33,21)

print(obj.perimeter())
print(obj.area())