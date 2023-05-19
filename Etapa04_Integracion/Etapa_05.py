from Etapa_01 import jugar, SUBPOSICION_DEFINICION_LISTA_DEFINICIONES,SUBPOSICION_PALABRA_LISTA_DEFINICIONES 
from Etapa_03 import Diez_letras_ordenadas, Definiciones_para_el_rosco


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
        lista_aciertos_y_errores.append(" ")                #*aca tira un error "list assignment index out of range" , porque esta fuera del rango
        posicion_lista_aciertos_y_errores += 1              #le pongo un append para que se solucione 
    return lista_aciertos_y_errores

def Seguir_jugando():
    """
    Esta función devuelve un valor booleano que sirve para verificar si el usuario quiere seguir jugando.
    Autor: Steven Guerrero
    """
    respuestas_positivas = ["SI","si","Si","sI","S","s","YES","Yes","yes","y","Y","true","True"]
    respuestas_negativas = ["No","NO","nO","no","n","N","false","False"]
    validacion = input("¿Desea seguir jugando? Escriba SI si desea seguir jugando, y escriba NO si desea salir:\n",)
    if validacion in respuestas_positivas:
        validacion = True
    elif validacion in respuestas_negativas:
        validacion = False
    #Falta agregar las excepciones
    return validacion

def Imprimir_resumen_de_juego(lista_letras, Lista_definiciones, lista_palabras_ingresadas, lista_aciertos_y_errores):
    """Esta función imprime en pantalla el resumen de la ronda.
    Esto incluye las 10 letras que se usaron en esta ronda, la palabra correcta a adivinar de cada letra
    y la palabra que ingresó el jugador en caso que se equivocara.
    Autor: Steven Guerrero
    Args:
        lista_letras (list): Es una lista compuesta por las 10 letras que se usaron para esta ronda del juego.
        Lista_definiciones (list): Una lista compuesta por las palabras y definiciones que son las respuestas correctas para esta ronda del juego. 
        lista_palabras_ingresadas (list): Una lista compuesta por las palabras que ingresó el jugador a lo largo de esta ronda.
        lista_aciertos_y_errores (list): Una lista compuesta por "a" y "e", indicando cuáles turnos el jugador acertó o se equivocó.
        posicion_turno (int): Variable numérica que sirve como contador para saber en cuál posición de las listas nos encontramos.
    """
    
    
    print("¡Ha concluido la partida!. Los resultados son:\n")
    for posicion_turno in range(0,len(lista_letras)):
        palabra_de_turno = Lista_definiciones[posicion_turno][SUBPOSICION_PALABRA_LISTA_DEFINICIONES]
        if lista_aciertos_y_errores[posicion_turno] == "a":
            print("Turno letra", lista_letras[posicion_turno], " - Palabra de ", len(palabra_de_turno)," letras - ", palabra_de_turno," - acierto")
        elif lista_aciertos_y_errores[posicion_turno] == "e":
            print("Turno letra", lista_letras[posicion_turno], " - Palabra de ", len(palabra_de_turno)," letras - ", lista_palabras_ingresadas[posicion_turno]," - error - Palabra Correcta: ", palabra_de_turno)
    return None




def comenzar_juego(dicc_palabras):
    """
    Esta funcion se encarga de empezar a correr la partida del juego
    Autor: Steven Guerrero  , colaboracion : Jonatan Misael Cruz
    """
    
    puntaje_final = 0
    Validacion_seguir_jugando = True #Una variable de control para determinar si el jugador sigue jugando o desea terminar la partida.

    while Validacion_seguir_jugando:
        Contador_aciertos = 0
        Contador_errores = 0
        puntaje = 0 #El jugador empieza con cero puntos su primera partida
        lista_palabras_ingresadas = [] #Una lista vacía que llevará registro de las palabras ingresadas por el jugador
        lista_letras = Diez_letras_ordenadas()#random.shuffle(Abecedario) #Se obtiene de funciones de la etapa 3
        posicion_turno = 0 #Turno en el que se encuentra el jugador ne este momento. Empieza en cero.
        Lista_definiciones = Definiciones_para_el_rosco(dicc_palabras, lista_letras) #Se obtiene de funciones de la etapa 3
        lista_aciertos_y_errores = Creacion_lista_vacia_aciertos_y_errores(lista_letras)
        Contador_aciertos, Contador_errores = jugar(lista_letras, lista_aciertos_y_errores, lista_palabras_ingresadas, Lista_definiciones, Contador_aciertos, Contador_errores, posicion_turno)
        Imprimir_resumen_de_juego(lista_letras, Lista_definiciones, lista_palabras_ingresadas, lista_aciertos_y_errores)
        puntaje_final += ((Contador_aciertos*10) - (Contador_errores*3))
        print("Puntaje final: ", puntaje_final)
        Validacion_seguir_jugando = Seguir_jugando()
        
            