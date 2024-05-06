'''
Ejercicio
Crear un decorador que, al aplicarlo sobre las funciones func1, func2 y func3, imprima por consola el nombre
de la funcion que esta siendo llamada, sin alterar el funcionamiento del programa original
'''


def decorador(f):
        print("Llamando a la función:", f.__name__)


def func1(n):
    decorador(func1)
    return n*2


def func2(n):
    decorador(func2)
    return n ** 2


def func3(n):
    decorador(func3)
    print(n)



if __name__ == '__main__':
    a = 5
    b = func1(a)
    c = func2(b)
    func3(c)
