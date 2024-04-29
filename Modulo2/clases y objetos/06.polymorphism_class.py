"""
Ejercicio 1.
Dado el siguiente código, cambiar las clases para que no falle al ser ejecutado
"""

class Car:
  on_board = 0

  def load_passangers(self, passengers, inspector = None):
    self.on_board = len(passengers)

class Bus:
  on_board = 0

  def load_passangers(self, passengers = None, inspectors = None):
    self.on_board = len(passengers) + len(inspectors)

class Bike:
  on_board = 0
  def load_passangers(self, passengers = None, inspectors = None):
    self.on_board = 1

""" DO NOT CHANGE AFTER THIS LINE """

def people_in_transit_on(vehicle, passengers, inspector):
  vehicle.load_passangers(passengers, inspector)

car_passengers = ['ruben', 'nieves']
bus_passengers = ['pepe', 'julia']
inspector = ['ramon']

car = Car()
bus = Bus()
bike = Bike()

people_in_transit_on(car, car_passengers, None)
people_in_transit_on(bus, car_passengers, inspector)
people_in_transit_on(bike, None, None)