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
        
        def Cant(self):
            return self.__cant
        
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