from Pila import Stack


def interseccion_de_pilas(pila1,pila2):
  interseccion = Stack()

  aux = set()
  while not pila1.size() == 0:
    aux.add(pila1.pop())

  while not pila2.size() == 0:
    personaje = pila2.pop()
    if personaje in aux:
      interseccion.push(personaje)

  return interseccion

episodio_V = Stack()
for i in range(5):
    Personajes_EpV = input("Ingrese personajes del Episodio V: ")
    episodio_V.push(Personajes_EpV)

print()
    
episodio_VII = Stack()
for i in range(5):
    Personajes_EpVII = input("Ingrese personajes del Episodio VII: " )
    episodio_VII.push(Personajes_EpVII)
    
interseccion = interseccion_de_pilas(episodio_V, episodio_VII)

print()

print("Los personajes que aparecen en ambos episodios son los siguientes:")
while not interseccion.size() == 0:
    print(interseccion.pop())
 