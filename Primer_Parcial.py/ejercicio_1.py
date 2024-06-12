def lista_inversa(lista):
  if len(lista) == 0:
    return []
  else:
    return [lista[-1]] + lista_inversa(lista[:-1])
  
Lista = [57,4,2,45,78,35,61,24,32,15]

print(Lista)
print("La lista inversa es:",lista_inversa(Lista))