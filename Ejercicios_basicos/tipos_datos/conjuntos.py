conjunto = {1,2,3,4}
conjunto = set(['a','b','c'])
conjunto = {1,2,3,3}

a = {1,2,3,4}
b = {3,4,5,6}
#union {1,2,3,4,5,6}
a|b

#interseccion {3,4}
a&b

#diferencia {1,2}
a-b

#diferencia simetrica {1,2,5,6}
a^b

conjunto.add(7)
conjunto.discard(4)
conjunto.clear()

#devuelve true si los valores estan dentro 
a.isdisjoint(b)

#si a esta en b
a.issubset(b)
#Devuelve True si A contiene , al menos , todos los elementos de B.
a.issuperset(b)

3 in a

#ejercicio 7

maria = ['GYD', 'DUS', 'PFO', 'ESB', 'GRX', 'HEL', 'BUD', 'KRR', 'SVQ', 'OLB', 'PSR', 'HEL', 'PFO', 'SVQ', 'LED']
luis = ['MXP', 'GRX', 'KIV', 'LIS', 'DUS', 'CWL', 'BRQ', 'HEL', 'BSL', 'IST', 'ESB', 'KRR', 'BSL', 'MXP', 'MXP', 'IST']

lista_maria = list(maria)
lista_luis = list(luis)

print(len(lista_maria))
print(len(lista_luis))

con_maria = set(lista_maria)
con_luis = set(lista_luis)
print(len(con_maria))
print(len(con_luis))


print(con_maria|con_luis ," , ", len(con_maria|con_luis))

print(con_maria-con_luis)

print(con_maria^con_luis," , ", con_maria&con_luis)