"""
Ejercicio 1.
Teneis que crear una clase con un método que guarde un número en un parametro de la clase.
Crear otro método en la clase que, dado un número por parametro, imprima la suma de ese númeor con el guardado por el metodo anterior.
Probar el código con multiples instancias de objetos.
"""

class num:
    def __init__(self,n1):
        self.n1 = n1
        
    def suma(self,n):
        return self.n1+n

obj1 = num(4)
suma = obj1.suma(4)
print(suma)