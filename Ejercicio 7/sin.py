from Cola import *
import random
from random import choice                                                                                                  

if __name__=='__main__':
    Cola_1 = Cola_Encadenada()
    Cola_2 = Cola_Encadenada()
    Cola_3 = Cola_Encadenada()
    Esperas_Atendidos = Cola_Encadenada()
    Esperas_No_Atendidos = Cola_Encadenada()
    Tiempo_total = 120
    cola1 = 0
    cola2 = 0
    cola3 = 0
    atencion_1 = 5
    atencion_2 = 3
    atencion_3 = 4
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
    while (Tiempo_total > 0):
        
        '''insertar clientes en cola segun los criterios dados'''
        if(llegada == 2):
            llegada = 0
            if (Cola_1.Vacia() == True) and (Cola_2.Vacia() == True) and (Cola_3.Vacia() == True):
                eleccion = random.randint(1,3)
                if eleccion == 1:
                    cola1 += 1
                    Cola_1.Insertar(0)
                elif eleccion == 2:
                    cola2 += 1
                    Cola_2.Insertar(0)
                elif eleccion == 3:
                    cola3 += 1
                    Cola_3.Insertar(0)
            else:
                if (Cola_1.Vacia() == True) and (Cola_2.Vacia() == True):
                    eleccion = random.randint(1,2)
                    if eleccion == 1:
                        cola1 += 1
                        Cola_1.Insertar(0)
                    elif eleccion == 2:
                        cola2 += 1
                        Cola_2.Insertar(0)
                else:
                    if (Cola_1.Vacia() == True) and (Cola_3.Vacia() == True):
                        eleccion = (choice([i for i in range(1,3) if i not in [2]]))
                        if eleccion == 1:
                            cola1 += 1
                            Cola_1.Insertar(0)
                        elif eleccion == 3:
                            cola3 += 1
                            Cola_3.Insertar(0)
                    else:
                        if (Cola_2.Vacia() == True) and (Cola_3.Vacia() == True):
                            eleccion = random.randint(1,2)
                            if eleccion == 1:
                                cola1 += 1
                                Cola_1.Insertar(0)
                            elif eleccion == 2:
                                cola2 += 1
                                Cola_2.Insertar(0)
                        else:
                            if (Cola_1.Vacia() == True):
                                cola1 += 1
                                Cola_1.Insertar(0)
                            else:
                                if (Cola_2.Vacia() == True):
                                    cola2 += 1
                                    Cola_2.Insertar(0)
                                else:
                                    if (Cola_3.Vacia() == True):
                                        cola3 += 1
                                        Cola_3.Insertar(0)
                                    else:
                                        if (cola1 < cola2) and (cola1 < cola3):
                                            cola1 += 1
                                            Cola_1.Insertar(0)
                                        else:
                                            if (cola2 < cola1) and (cola2 < cola3):
                                                cola2 += 1
                                                Cola_2.Insertar(0)
                                            else:
                                                if (cola3 < cola1) and (cola3 < cola2):
                                                    cola3 += 1
                                                    Cola_3.Insertar(0)
                                                else:
                                                    if (cola1 < cola3) and (cola1 == cola2):
                                                        eleccion = random.randint(1,2)
                                                        if eleccion == 1:
                                                            cola1 += 1
                                                            Cola_1.Insertar(0)
                                                        elif eleccion == 2:
                                                            cola2 += 1
                                                            Cola_2.Insertar(0)
                                                    else:
                                                        if (cola1 < cola2) and (cola1 == cola3):
                                                            eleccion = (choice([i for i in range(1,3) if i not in [2]]))
                                                            if eleccion == 1:
                                                                cola1 += 1
                                                                Cola_1.Insertar(0)
                                                            elif eleccion == 3:
                                                                cola3 += 1
                                                                Cola_3.Insertar(0)
                                                        else:
                                                            if (cola2 < cola1) and (cola2 == cola3):
                                                                eleccion = random.randint(2,3)
                                                                if eleccion == 2:
                                                                    cola2 += 1
                                                                    Cola_2.Insertar(0)
                                                                elif eleccion == 3:
                                                                    cola3 += 1
                                                                    Cola_3.Insertar(0)
        if ((Cola_1.Vacia() == False)):
            if (atencion_1 != 5):
                atencion_1 += 1
            else:
                atencion_1 = 0
                x = Cola_1.Suprimir()
                Esperas_Atendidos.Insertar(x)
                atendidos += 1
                cola1 -= 1
        if ((Cola_2.Vacia() == False)):
            if (atencion_2 != 3):
                atencion_2 += 1
            else:
                atencion_2 = 0
                y = Cola_2.Suprimir()
                Esperas_Atendidos.Insertar(x)
                atendidos += 1
                cola2 -= 1
        if ((Cola_3.Vacia() == False)):
            if (atencion_3 != 4):
                atencion_3 += 1
            else:
                atencion_3 = 0
                z = Cola_3.Suprimir()
                Esperas_Atendidos.Insertar(x)
                atendidos += 1
                cola3 -= 1
        
        '''incrementa los tiempos de espera de cada cliente en cola'''
        aux = 0
        while (aux != cola1):
            w = Cola_1.Suprimir()
            w += 1
            Cola_1.Insertar(w)
            aux += 1
        aux = 0
        while (aux != cola2):
            w = Cola_2.Suprimir()
            w += 1
            Cola_2.Insertar(w)
            aux += 1
        aux = 0
        while (aux != cola3):
            w = Cola_3.Suprimir()
            w += 1
            Cola_3.Insertar(w)
            aux += 1
        
        '''ajusta variables de control'''
        llegada += 1
        Tiempo_total -= 1
    
    '''fin de la simulacion'''
    print("La simulacion ha terminado")
    no_atendidos = cola1 + cola2 + cola3
    
    '''calcular promedio de espera de clientes atendidos y buscar el maximo'''
    while (Esperas_Atendidos.Vacia() == False):
        a = Esperas_Atendidos.Suprimir()
        prom_espera_atendidos += a
        if (a > max1):
            max1 = a
    prom_espera_atendidos = prom_espera_atendidos // atendidos
    
    '''cargar tiempos de esperas de no atendidos'''
    while (Cola_1.Vacia() == False):
        Esperas_No_Atendidos.Insertar(Cola_1.Suprimir())
    while (Cola_2.Vacia() == False):
        Esperas_No_Atendidos.Insertar(Cola_2.Suprimir())
    while (Cola_3.Vacia() == False):
        Esperas_No_Atendidos.Insertar(Cola_3.Suprimir())
    
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
    print(f"Tiempo de espera promedio de clientes atendidos:{prom_espera_atendidos} minutos")
    print(f"Cantidad de clientes sin atender: {no_atendidos}")
    print(f"Tiempo de espera promedio de clientes no atendidos: {prom_espera_no_atendidos} minutos")
    print(f"Tiempo de espera maximo: {max_total} minutos")