from Cola import *
import random

if __name__=='__main__':
    Cola_de_Impresion = Cola_Encadenada()
    Tiempos_espera = Cola_Encadenada()
    Espera_Completa = Cola_Encadenada()
    Impresora = 0
    Tiempo_total = int(input('Ingrese tiempo maximo de simulacion: '))
    i = 0
    llegada = 0
    terminados = 0
    prom_espera = 0
    
    while (i < Tiempo_total):
        '''Insertar a la cola'''
        llegada = random.random()
        if ((0 <= llegada) and (llegada <= (1/5))):
            trabajo = random.randint(1, 10)
            Cola_de_Impresion.Insertar(trabajo)
            Tiempos_espera.Insertar(i)
        
        '''suprimir de la cola'''
        if (Impresora == 0):
            if (Cola_de_Impresion.Vacia() == False):
                actual = Cola_de_Impresion.Suprimir()
                x = Tiempos_espera.Suprimir()
                espera = i - x
                Impresora += 1
        else:
            if (Impresora < 5):
                actual -= 1
                Impresora += 1
            else:
                Impresora = 0
                if (actual > 0):
                    Cola_de_Impresion.Insertar(actual)
                    Tiempos_espera.Insertar(espera + i)
                else:
                    terminados += 1
                    espera = i-x
                    Espera_Completa.Insertar(espera)
        
        '''ajustar las variables de control'''
        i += 1
    print("La simulacion termino")
    while (Espera_Completa.Vacia() == False):
        prom_espera += Espera_Completa.Suprimir()
    prom_espera = prom_espera // terminados
    print(f"Cantidad de trabajos sin terminar: {Cola_de_Impresion.Cant()}")
    print(f"Promedio de espera de los trabajos terminados: {prom_espera} minutos")