from TP3.listaej6 import Lista
l =Lista()

class Superheroe:

  def __init__(self, nombre ,casa,aparicion,biografia):
      self.nombre = nombre
      self.aparicion = aparicion
      self.casa = casa
      self.biografia = biografia

  def __str__(self):
      return f"{self.nombre},{self.casa},{self.aparicion},{self.biografia}"

heroes = [
    {'name': 'iron man', 'anio': 1961,'casa':'Marvel','bio': 'usa un traje de hierro'},
    {'name': 'capitan america', 'anio': 1973,'casa':'Marvel','bio': 'tiene un escudo de vibranio'},
    {'name': 'batman', 'anio': 1975,'casa':'DC','bio': '....'},
    {'name': 'LINTERNA VERDE', 'anio': 1979,'casa':'DC','bio': 'completar la bio'},
    {'name': 'wolverine', 'anio': 1966,'casa':'Marvel','bio': 'pertenece a los x-men'},
    {'name': 'dr. strange', 'anio': 1970,'casa':'DC','bio': '...'},
    {'name': 'mujer maravilla', 'anio': 1960,'casa':'DC','bio': '...'}
]

for heroe in heroes:
  l.insert(Superheroe(heroe['name'].title() ,heroe['casa'],heroe['anio'],heroe['bio']), 'nombre')

#a)
#title por case sensitive
dato = l.remove('linterna verde'.title(), 'nombre')
if(dato):
    print(f'el superheroe {dato.nombre} fue eliminado')
else:
    print('el superheroe no esta en la lista')
#b
dato = l.search('wolverine'.title(),'nombre')
if(dato):
    print(f'el superheroe {dato.info.nombre} apareció en {dato.info.aparicion}')
else:
    print('el superheroe no esta en la lista')
#c
#si el campo a modificar no es el campo clave puedo modificarlo directamente, sino hay que removelo y volver a insert
dato = l.search('dr. strange'.title(), 'nombre')
if(dato):
    dato.info.casa = 'Marvel'
    print(f'el superheroe {dato.info.nombre} fue modificado')
else:
    print('el superheroe no esta en la lista')
#D

#l.barrido_traje_armadura()

#E
#l.barrido_anterior_1963()

#F
dato = l.search('mujer maravilla'.title(),'nombre')
if(dato):
    print(f'la {dato.info.nombre} pertenece a la casa {dato.info.casa}')
else:
    print('el superheroe no esta en la lista')

dato = l.search('capitana marvel'.title(),'nombre')
if(dato):
    print(f'la {dato.info.nombre} pertenece a la casa {dato.info.casa}')
else:
    print('el superheroe no esta en la lista')

#h
print()
l.barrido_start_with(['B','M','S'])

marvel,dc = l.contar_por_casa()
print(f"cantidad de superheroes de marvel {marvel} y de dc {dc}")