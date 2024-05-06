from errors import ElementAlreadyInListError

elements = [1, 5, -2]


def add_once(list, element):
    try:
        if element in list:
            raise ElementAlreadyInListError(element)
        else:
            list.append(element)
    except ElementAlreadyInListError as error:
        print("error imposible añadir elementos repetidos ", error.args[0])


add_once(elements, 10)
add_once(elements, -2)
add_once(elements, "This is a test")

print(elements)
