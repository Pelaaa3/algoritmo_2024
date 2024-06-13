class nodoPila(): #representa cada elemento
    info, sig = None, None #datos, direccion de memoria  #siguiente apunta al anterior

class Pila(): #representa la estructura de datos

    def __init__(self): #constructor
        self.__tamanio = 0 #atributo privado, no se puede editar fuera de la clase; se tiene que usar los metodos de la clase
        self.__cima = None #direccion de memoria
    
    def tamanio(self):
        return self.__tamanio
        
    def apilar(self, elemento):
        nodo = nodoPila()
        nodo.info = elemento
        nodo.sig = self.__cima
        self.__cima = nodo

        self.__tamanio += 1

    def cima(self):
        return self.__cima.info

    def pila_vacia(self):
        return self.__cima == None #se puede hacer con tamanio == 0
    
    def desapilar(self):
        dato = self.__cima.info
        self.__cima = self.__cima.sig
        self.__tamanio -= 1

        return dato
