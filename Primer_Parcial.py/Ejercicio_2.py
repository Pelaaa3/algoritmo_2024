# 2. Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:
# a) Contar cuantas especies hay;
# b) Determinar cuantos descubridores distintos hay;
# c) Mostrar todos los dinosaurios que empiecen con T;
# d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
# e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;
from cola import *

def __init__(self,especie,descubridor,ano_descubrimiento,peso,nombre):
  self.especie = especie
  self.descubridor = descubridor
  self.peso = peso
  self.nombre = nombre
  self.ano_descubrimiento = ano_descubrimiento
  
dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": "7000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": "6000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": "15 kg",
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": "56000 kg",
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": "5000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": "10000 kg",
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": "2000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": "23000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": "15000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": "6000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": "2500 kg",
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": "1500 kg",
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": "2700 kg",
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": "5000 kg",
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": "25 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": "200 kg",
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": "450 kg",
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": "15000 kg",
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]

#Punto A  
def especies(dinosaurios):
  especie = set()
  for dinos in dinosaurios:
    especie.add(dinos["especie"])
  return len(especie)

cantidad_especies = especies(dinosaurios)
print("La cantidad de especies de dinosaurios que aparecen en la lista es:",cantidad_especies)

print()
print()

#Punto B
def descubridores(dinosaurios):
  descubridores = set()
  for descubridor in dinosaurios:
    descubridores.add(descubridor["descubridor"])
  return len(descubridores)

cantidad_descubridores = descubridores(dinosaurios)
print("La cantidad de descubridores de dinosaurios que aparecen en la lista es:",cantidad_descubridores)

print()
print()

#Punto C
print("Los dinosaurios que empiezan con la Letra T son:")
for dinos in dinosaurios:
  if dinos["nombre"].startswith("T"):
    print(dinos["nombre"])
    
print()
print()
    
#Punto D
Pila_peso = Queue()
for dinos in dinosaurios:
  peso = int(dinos["peso"].split()[0])
  if peso < 275:
    Pila_peso.arrive(dinos)

print("Dinosaurios con peso menor a 275 KG:")
while Pila_peso.size() > 0:
  dinos = Pila_peso.attention()
  print(dinos["nombre"])

print()
print()

#Punto E
Pila_dinosaurios = Queue()

for dinos in dinosaurios:
  nombre = dinos["nombre"]
  if nombre.startswith(("A","Q","S")):
    Pila_dinosaurios.arrive(dinos)

print("Los dinosaurios que empiezan con A, Q y S son:")
while Pila_dinosaurios.size() > 0:
  dinos = Pila_dinosaurios.attention()
  print(dinos["nombre"])  

  