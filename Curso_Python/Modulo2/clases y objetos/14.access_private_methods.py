"""
Ejercicio 1.
Tratar de acceder al metodo y paremetro privado de la siguiente clase sin usar otros métodos.
"""

class PrivateStuff:
  __private_parameter = 'private'

  def __private_function(self):
    print('I am private')
    

obj = PrivateStuff()
obj._PrivateStuff__private_function()
print(PrivateStuff._PrivateStuff__private_parameter)
