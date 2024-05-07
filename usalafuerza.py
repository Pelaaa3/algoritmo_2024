mochila = ["casco","cuchillo","linterna","sable de luz","comida","mapa"]

def usar_la_fuerza(mochila):# si encontro el sable de luz y la posicion
    if(len(mochila) == 0): #no encontro el sable de luz
        return False, 0
    elif(mochila[0] == "sable de luz"):
        return True, 0
    else:
        recursiva = usar_la_fuerza(mochila[1:])
        return recursiva[0], recursiva[1] +1

objetos_sacados = usar_la_fuerza(mochila)
if(objetos_sacados[0]):
    print("Se encontró el sable de luz dentro de la mochila y fue necesario sacar",objetos_sacados[1],"objetos")
else:
    print("No se encontro el sable de luz en la mochila")
   
    


