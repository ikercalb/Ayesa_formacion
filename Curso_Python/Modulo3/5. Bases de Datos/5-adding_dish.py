import sqlite3


def add_dish(dish_name, category_name):
    #TODO: Completad este método
    conexion = sqlite3.connect('restaurants.db')
    cursor = conexion.cursor()

    cursor.execute('Select * from category where name = ?', (category_name,))
    id = cursor.fetchone()
    id = id[0]
    cursor.execute('INSERT INTO dish (name,category_id) VALUES (?,?)', (dish_name, id,))
    conexion.commit()
    cursor.execute('Select * from dish ')

    dishes = cursor.fetchall()
    print(dishes)
    conexion.close()


add_dish("sopa", "starter")
add_dish("burger", "principal")
add_dish("helado", "dessert")
