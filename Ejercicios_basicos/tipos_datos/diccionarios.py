entrenadores = {'Madrid': 'Zidane', 'Barcelona':'Valverde', 'Getafe':'Bordalas'}
entrenadores.get('Madrid')

#devuelve el valor y lo elimina del diccionario
entrenadores.pop('Madrid')

#inserta o actualiza la clave-valor
entrenadores.update({'Sevilla':'caparros'})

'Sevilla' in entrenadores

entrenadores.keys()
entrenadores.values()
entrenadores.items()

entrenadores.clear()

#ejercicio 6 

personas = {1:'Jose',2:'Adrian'}
personas.update({3:'Gloria'})
personas.update({1:'Jose manuel'})
personas.pop(2)
print(personas.keys())

