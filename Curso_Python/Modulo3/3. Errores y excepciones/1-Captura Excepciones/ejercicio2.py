try:
    colours = { 'rojo':'red', 'verde':'green', 'negro':'black' }
    colours['blanco']
except KeyError:
    print("No existe ese valor")