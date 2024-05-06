

import pares
import Impares

from subpaquete import * # Hacemos la llamada directamente al subpaquete y podemos acceder a todas las clases que estan escritas en su __init__

print(pares.par(1,8))
print(Impares.impar(1,8))

print(resta.resta(8,4))

# No funciona porque no se encuentra en el __init__
print(suma.suma(4,3))

