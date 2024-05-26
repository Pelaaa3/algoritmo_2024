# Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su name y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos name empiezan con C, D y G.
class Personaje:
    def __init__(self, name, cantidad_pelis):
        self.name = name
        self.cantidad_pelis = cantidad_pelis
    
    def __str__(self):
        return f"{self.name} {self.cantidad_pelis}"

personajes = [
    {'name': 'Rocket Raccoon', 'pelis': 4},
    {'name': 'Iron Man', 'pelis': 6},
    {'name': 'Capitan America', 'pelis': 5},
    {'name': 'Groot', 'pelis': 4},
    {'name': 'Black Widow', 'pelis': 7},
    {'name': 'Loki', 'pelis': 4},
]
from Pila import Stack
pila = Stack()
for pers in personajes:
    pila.push(Personaje(pers['name'],pers['pelis']))

iniciales = ['C','D','G']
pos = pila.size()+1
while(not pila.vacia()):
    pos -= 1
    dato = pila.pop()
    if(dato.name == "Rocket Raccoon" or dato.name == "Groot"):
        print(dato.name,"se encuentra en la posicion",pos)
    elif(dato.name == "Black Widow"):
        print("Black Widow participo en",dato.cantidad_pelis,"peliculas")
    if(dato.cantidad_pelis > 5):
        print(dato.name,"participo en",dato.cantidad_pelis,"peliculas")
    if(dato.name[0] in iniciales):
        print(dato)