from Cola import *
import random
from random import choice                                                                                                  

if __name__=='__main__':
    Cola_1 = Cola_Encadenada()
    Cola_2 = Cola_Encadenada()
    Cola_3 = Cola_Encadenada()
    Cajero_1 = 0
    Cajero_2 = 0
    Cajero_3 = 0
    Esperas_Atendidos = Cola_Encadenada()
    Esperas_No_Atendidos = Cola_Encadenada()
    Tiempo_total = 0
    llegada = 0
    atendidos = 0
    no_atendidos = 0
    prom_espera_atendidos= 0
    prom_espera_no_atendidos = 0
    w = 0
    x = 0
    y = 0
    z = 0
    a = 0
    b = 0
    max1 = 0
    max2 = 0
    max_total = 0
    while (Tiempo_total < 120):
        
        '''insertar clientes en cola segun los criterios dados'''
        llegada = random.random()
        if((0 <= llegada) and (llegada <= (1/2))):
            if (Cola_1.Cant() == Cola_2.Cant()) and (Cola_2.Cant() == Cola_3.Cant()):
                eleccion = random.randint(1,3)
                if eleccion == 1:
                    Cola_1.Insertar(Tiempo_total)
                elif eleccion == 2:
                    Cola_2.Insertar(Tiempo_total)
                elif eleccion == 3:
                    Cola_3.Insertar(Tiempo_total)
            else:
                if (Cola_1.Cant() < Cola_2.Cant()) and (Cola_1.Cant() < Cola_3.Cant()):
                    Cola_1.Insertar(Tiempo_total)
                else:
                    if (Cola_2.Cant() < Cola_1.Cant()) and (Cola_2.Cant() < Cola_3.Cant()):
                        Cola_2.Insertar(Tiempo_total)
                    else:
                        if (Cola_3.Cant()< Cola_1.Cant()) and (Cola_3.Cant() < Cola_2.Cant()):
                            Cola_3.Insertar(Tiempo_total)
                        else:
                            if (Cola_1.Cant() < Cola_3.Cant()) and (Cola_1 == Cola_2.Cant()):
                                eleccion = random.randint(1,2)
                                if eleccion == 1:
                                    Cola_1.Insertar(Tiempo_total)
                                elif eleccion == 2:
                                    Cola_2.Insertar(Tiempo_total)
                            else:
                                if (Cola_1.Cant() < Cola_2.Cant()) and (Cola_1.Cant() == Cola_3.Cant()):
                                    eleccion = (choice([i for i in range(1,3) if i not in [2]]))
                                    if eleccion == 1:
                                        Cola_1.Insertar(Tiempo_total)
                                    elif eleccion == 3:
                                        Cola_3.Insertar(Tiempo_total)
                                else:
                                    if (Cola_2.Cant() < Cola_1.Cant()) and (Cola_2.Cant() == Cola_3.Cant()):
                                        eleccion = random.randint(2,3)
                                        if eleccion == 2:
                                            Cola_2.Insertar(Tiempo_total)
                                        elif eleccion == 3:
                                            Cola_3.Insertar(Tiempo_total)
        '''Manejo de las colas'''
        
        if ((Cajero_1 == 0)):
            if (Cola_1.Vacia() == False):
                Cajero_1 += 1
                x = Cola_1.Suprimir()
                Espera = Tiempo_total - x
                Esperas_Atendidos.Insertar(Espera)
                atendidos += 1
        else:
            if (Cajero_1 < 5):
                Cajero_1 += 1
            else:
                Cajero_1 = 0
        
        if ((Cajero_2 == 0)):
            if (Cola_2.Vacia() == False):
                x = Cola_2.Suprimir()
                Cajero_2 += 1
                Espera = Tiempo_total - x
                Esperas_Atendidos.Insertar(Espera)
                atendidos += 1
        else:
            if (Cajero_2 < 3):
                Cajero_2 += 1
            else:
                Cajero_2 = 0
        
        if ((Cajero_3 == 0)):
            if (Cola_3.Vacia() == False):
                Cajero_3 += 1
                x = Cola_3.Suprimir()
                Espera = Tiempo_total - x
                Esperas_Atendidos.Insertar(Espera)
                atendidos += 1
        else:
            if (Cajero_3 < 4):
                Cajero_3 += 1
            else:
                Cajero_3 = 0
        
        '''ajusta variables de control'''
        Tiempo_total += 1
    
    '''fin de la simulacion'''
    print("La simulacion ha terminado")
    
    '''calcular promedio de espera de clientes atendidos y buscar el maximo'''
    while (Esperas_Atendidos.Vacia() == False):
        a = Esperas_Atendidos.Suprimir()
        prom_espera_atendidos += a
        if (a > max1):
            max1 = a
    prom_espera_atendidos = prom_espera_atendidos // atendidos
    
    '''cargar tiempos de esperas de no atendidos'''
    while (Cola_1.Vacia() == False):
        x = Cola_1.Suprimir()
        Espera = Tiempo_total - x
        Esperas_No_Atendidos.Insertar(Espera)
        no_atendidos += 1
    while (Cola_2.Vacia() == False):
        x = Cola_2.Suprimir()
        Espera = Tiempo_total - x
        Esperas_No_Atendidos.Insertar(Espera)
        no_atendidos += 1
    while (Cola_3.Vacia() == False):
        x = Cola_3.Suprimir()
        Espera = Tiempo_total - x
        Esperas_No_Atendidos.Insertar(Espera)
        no_atendidos += 1
    
    '''calcular promedio de espera de clientes no atendidos y buscar el maximo'''
    while (Esperas_No_Atendidos.Vacia() == False):
        b = Esperas_No_Atendidos.Suprimir()
        prom_espera_no_atendidos += b
        if (b > max2):
            max2 = b
    prom_espera_no_atendidos = prom_espera_no_atendidos // no_atendidos
    
    '''busca el tiempo de espera maximo'''
    if (max1 > max2):
        max_total = max1
    else:
        max_total = max2
    
    print(f"Cantidad de clientes atendidos: {atendidos}")
    print(f"Tiempo de espera promedio de clientes atendidos: {prom_espera_atendidos} minutos")
    print(f"Cantidad de clientes sin atender: {no_atendidos}")
    print(f"Tiempo de espera promedio de clientes no atendidos: {prom_espera_no_atendidos} minutos")
    print(f"Tiempo de espera maximo: {max_total} minutos")