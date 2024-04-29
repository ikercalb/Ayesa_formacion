"""
Ejercicio 1.
Teneis que crear una clase con un constructor que guarde un número N y un string S.
Crear otro método que imprima los primeros N caracteres del string S.
Probar con multiples instancias de objetos.
"""

class ejercicio1:
    def __init__(self,n,s):
        self.n = n 
        self.s = s

    def caracteres(self):
        return self.s[:self.n]
    
    def cambion(self,n):
        self.n = n
    def cambios(self,s):
        self.s = s

obj = ejercicio1(3,'manolo')
print(obj.caracteres())

"""
Ejercicio 2.
Ampliar la clase anterior con dos métodos que cambien el valor de N y S, respectivamente.
Probar que cuandos se cambia el valor cambia el valor que imprime el método creado en el ejercicio anterior.
"""

obj.cambion(4)
print(obj.caracteres())
obj.cambios("antonio")
print(obj.caracteres())