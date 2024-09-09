import numpy as np

class Cola_Secuencial:
    __dimension = 0
    __cola = None
    __tope = 0
    __cantidad = 0

    def __init__(self, dimension):
        self.__cola = np.empty(dimension, dtype=int)
        self.__tope = 0
        self.__dimension = dimension
        self.__primero = 0
        self.__ultimo = 0
    
    def Vacia(self):
        return self.__cantidad == 0
    
    def Insertar(self, x):
        retorna = 0
        if (self.__cantidad <= self.__dimension):
            self.__cola[self.__ultimo] = x
            self.__ultimo = (self.__ultimo + 1) % self.__dimension
            self.__cantidad += 1
            retorna = x
        else:
            print("Tenes la cola llena jaja \n")
        return retorna
    
    def Suprimir(self):
        retorna = 0
        if (self.Vacia() == False):
            x = self.__cola[self.__primero]
            self.__primero = (self.__primero + 1) % self.__dimension
            self.__cantidad -= 1
            retorna = x
            '''i = 0
            x = self.__cola[0]
            retorna = x
            for i in range (self.__tope - 1):
                self.__cola[i]=self.__cola[i+1]
            self.__cantidad -= 1
            self.__tope -= 1'''
        else: 
            print("La cola está vacia \n")
        return retorna
    
    def Recorrer(self):
        if (self.Vacia() == False):
            i = self.__primero
            j = 0
            while (j < self.__cantidad):
                print (self.__cola[i])
                i = (i + 1) % self.__dimension
                j += 1


class Nodo:
    def __init__(self):
        self.__item = 0
        self.__sig = None

    def getItem(self):
        return self.__item

    def cargaItem(self, unItem):
        self.__item = unItem

    def cargaSig(self, sig):
        self.__sig = sig

    def getSig(self):
        return self.__sig

class Cola_Encadenada:
        __primero : Nodo
        __ultimo : Nodo
        __cant : int
        def __init__(self):
            self.__cant = 0
            self.__primero = None
            self.__ultimo = None
        
        def Vacia(self):
            return self.__cant == 0
        
        def Insertar(self, x):
            Elemento = Nodo()
            Elemento.cargaItem(x)
            Elemento.cargaSig(None)
            if (self.__ultimo == None):
                self.__primero = Elemento
            else:
                self.__ultimo.cargaSig(Elemento)
            self.__ultimo = Elemento
            self.__cant += 1
        
        def Suprimir(self):
            retorna = None
            if (self.Vacia() == False):
                x = self.__primero.getItem()
                self.__primero = self.__primero.getSig()
                self.__cant -= 1
                retorna = x
                if (self.__primero == None):
                    self.__ultimo = None
            else:
                print("Tenes la cola vacia")
            return retorna
        
        def Recorrer(self):
            aux = self.__primero
            while(aux != None):
                print(f"{aux.getItem()}")
                aux = aux.getSig()