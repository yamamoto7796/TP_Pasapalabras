from Etapa_01 import *
import Etapa_09
import Etapa_07
import time

def Creacion_lista_vacia_aciertos_y_errores(lista_letras):
    """
    Esta función crea una lista vacía, la cual se va se usará como la lista inicial de de aciertos y errores con la que interactuará el jugador al iniciar el juego.
    Autor: Steven Guerrero
    >>> Creacion_lista_vacia_aciertos_y_errores(["A","B","C"])
    [" "," "," "]
    >>> Creacion_lista_vacia_aciertos_y_errores(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
    [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    >>> Creacion_lista_vacia_aciertos_y_errores(["A"])
    [" "]
    >>> Creacion_lista_vacia_aciertos_y_errores([" "])
    [" "]
    >>> Creacion_lista_vacia_aciertos_y_errores([])
    []
    >>> Creacion_lista_vacia_aciertos_y_errores(["A","B","C","D","E","F","G","H","I","J"])
    [" "," "," "," "," "," "," "," "," "," "]    
    """
    lista_aciertos_y_errores = []
    posicion_lista_aciertos_y_errores = 0
    while len(lista_aciertos_y_errores) < len(lista_letras):
        lista_aciertos_y_errores.append(" ")                
        posicion_lista_aciertos_y_errores += 1              
    return lista_aciertos_y_errores

def Seguir_jugando(puntaje_final,contador):
    MAX_PARTIDAS = int(Etapa_09.MAX_PARTIDAS)
    """
    Esta función devuelve un valor booleano que sirve para verificar si el usuario quiere seguir jugando.
    Autor: Steven Guerrero
    """
    respuestas_positivas = ["SI","si","Si","sI","S","s","YES","Yes","yes","y","Y","true","True"]
    respuestas_negativas = ["No","NO","nO","n", "no","N","false","False"]
    respuesta = input("¿Desea seguir jugando? Escriba SI si desea seguir jugando, y escriba NO si desea salir:\n",)
    volver_a_preguntar = True
    while volver_a_preguntar and contador <= MAX_PARTIDAS:
        if respuesta in respuestas_positivas:
            validacion = True
            volver_a_preguntar = False
            contador += 1
        elif respuesta in respuestas_negativas:
            validacion = False
            volver_a_preguntar = False
            imprimir_puntaje_final(puntaje_final)
        else:
            respuesta = input("Debe elegir una de las 2 opciones, ¿desea seguir jugando? Escriba SI si desea seguir jugando, y escriba NO si desea salir:\n",)
    if contador > MAX_PARTIDAS:
        print("Reporte final:")
        print("Partidas Jugadas:",contador)
        print()
        print()
        imprimir_puntaje_final(puntaje_final)
        time.sleep(8)
        validacion = False

    return validacion, contador

def Imprimir_resumen_de_juego(lista_letras, lista_definiciones, lista_palabras_ingresadas, lista_aciertos_y_errores,lista_turnos):
    """Esta función imprime en pantalla el resumen de la ronda.
    Esto incluye las 10 letras que se usaron en esta ronda, la palabra correcta a adivinar de cada letra
    y la palabra que ingresó el jugador en caso que se equivocara.
    Autor: Steven Guerrero
    Actualizacion: Jose Adrian
    Args:
        lista_letras (list): Es una lista compuesta por las 10 letras que se usaron para esta ronda del juego.
        Lista_definiciones (list): Una lista compuesta por las palabras y definiciones que son las respuestas correctas para esta ronda del juego. 
        lista_palabras_ingresadas (list): Una lista compuesta por las palabras que ingresó el jugador a lo largo de esta ronda.
        lista_aciertos_y_errores (list): Una lista compuesta por "a" y "e", indicando cuáles turnos el jugador acertó o se equivocó.
        posicion_turno (int): Variable numérica que sirve como contador para saber en cuál posición de las listas nos encontramos.
    """
    print("¡Ha concluido la partida!. Los resultados son:\n")
    for posicion_turno in range(0,len(lista_letras)):
        palabra_de_turno = lista_definiciones[posicion_turno][SUBPOSICION_PALABRA_LISTA_DEFINICIONES]
        pos_jugador_actual = (int(lista_turnos[posicion_turno])-1)
        if lista_aciertos_y_errores[posicion_turno] == "a":
            print("Turno letra", lista_letras[posicion_turno]," - Jugador ",lista_turnos[posicion_turno]," ",Etapa_07.Lista_Jugadores[pos_jugador_actual]," - Palabra de ", len(palabra_de_turno)," letras - ", palabra_de_turno," - acierto")
        elif lista_aciertos_y_errores[posicion_turno] == "e":
            print("Turno letra", lista_letras[posicion_turno]," - Jugador ",lista_turnos[posicion_turno]," ",Etapa_07.Lista_Jugadores[pos_jugador_actual]," - Palabra de ", len(palabra_de_turno)," letras - ", lista_palabras_ingresadas[posicion_turno]," - error - Palabra Correcta: ", palabra_de_turno)
    return None

def imprimir_puntaje_ronda(puntaje_ronda):
    """
    Esta funcion se encarga de imprimir el puntaje de la ronda actual.
    Autor:Facundo Cabral
    """
    print("Puntaje parcial:")
    for i,jugador in enumerate(Etapa_07.Lista_Jugadores,1):
        print(i,". ",jugador," - ",puntaje_ronda[i-1], "puntos")
    print()
    print()

def actualizar_puntaje(puntaje_final,puntaje_ronda):
    """
    Esta funcion se encarga de imprimir el puntaje de toda la partida.
    Autor:Jose Adrian
    """
    for puntos_jugador in range(len(puntaje_final)):
        puntaje_final[puntos_jugador] += puntaje_ronda[puntos_jugador]
    return puntaje_final

def imprimir_puntaje_final(puntaje_final):
    print("Puntaje de la partida:")
    for i,jugador in enumerate(Etapa_07.Lista_Jugadores,1):
        print(i,". ",jugador," - ",puntaje_final[i-1], "puntos")

def comenzar_partida(lista_letras, lista_definiciones, puntaje_final,contador):
    """
    Esta funcion se encarga de empezar a correr la partida del juego
    Autor: Steven Guerrero  , colaboracion : Jonatan Misael Cruz
    Actualizacion 2da Parte: Facundo Cabral
    """
    lista_turnos = Etapa_09.Crear_Lista_Turnos(lista_letras)
    estadisticas = Etapa_09.Crear_Estadisticas(Etapa_07.Lista_Jugadores)
    puntaje_ronda = Etapa_09.Crear_Puntaje_Ronda(Etapa_07.Lista_Jugadores)
    lista_palabras_ingresadas = [] #Una lista vacía que llevará registro de las palabras ingresadas por el jugador
    posicion_turno = 0 #Turno en el que se encuentra el jugador ne este momento. Empieza en cero.
    jugador_turno = 0 #Es el turno del jugador actual.
    lista_aciertos_y_errores = Creacion_lista_vacia_aciertos_y_errores(lista_letras)
    estadisticas = jugar(lista_letras, lista_aciertos_y_errores, lista_palabras_ingresadas, lista_definiciones, estadisticas, posicion_turno, jugador_turno,lista_turnos,puntaje_ronda)
    Imprimir_resumen_de_juego(lista_letras, lista_definiciones, lista_palabras_ingresadas, lista_aciertos_y_errores,lista_turnos)
    puntaje_final = actualizar_puntaje(puntaje_final,puntaje_ronda)
    imprimir_puntaje_ronda(puntaje_ronda)
    imprimir_puntaje_final(puntaje_final)
    seguir_jugando,contador = Seguir_jugando(puntaje_final,contador)
    return seguir_jugando, puntaje_final,contador