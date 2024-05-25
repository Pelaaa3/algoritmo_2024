#5. Desarrollar una función que permita convertir un número romano en un número decimal.

valor ={'I': 1, 'V':5,'X': 10, 'L': 50, 'C': 100}
romano = input('ingrese el numero romano que desea convertir en mayusculas:')
def num_romano(romano):
   if (len(romano)== 1):
       return valor[romano[0]]
   elif (valor[romano[0]] >= valor[romano[1]]):
       return valor[romano[0]] + num_romano(romano[1:])
   else:
        return -valor[romano[0]] + num_romano(romano[1:])

print(num_romano(romano))