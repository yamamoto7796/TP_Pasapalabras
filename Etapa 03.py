import random
from datos import *
SUBPOSICION_PALABRA_LISTA_DEFINICIONES = 0 #posición de la palabra de turno en el array de palabras y definiciones
SUBPOSICION_DEFINICION_LISTA_DEFINICIONES = 1 #posición de la definición de turno en el array de palabras y definiciones

def Validar_palabra_ingresada(palabra):
    """
    Esta función valida que la palagra ingresada por el usuario no contiene números, caractéres especiales, ni espacios, solamente letras.
    Autor: Steven Guerrero
    >>> Validar_palabra_ingresada("ñame")
    True
    >>> Validar_palabra_ingresada("corazón")
    True
    >>> Validar_palabra_ingresada("zapato")
    True
    >>> Validar_palabra_ingresada("Mayúscula")
    True
    >>> Validar_palabra_ingresada("1amarre")
    False
    >>> Validar_palabra_ingresada("palabra de prueba")
    False
    >>> Validar_palabra_ingresada("*palabrota")
    False
    >>> Validar_palabra_ingresada("* Ahora T0d0 Junt0 +")
    False
    """
    validador01 = palabra.isalpha()
    return validador01

def Validar_longitud_palabra_ingresada(palabra,longitud):
    """
    Esta función valida que la palagra ingresada por el usuario no contiene números, caractéres especiales, ni espacios, solamente letras.
    Autor: Steven Guerrero
    >>> Validar_longitud_palabra_ingresada("ñame",4)
    True
    >>> Validar_longitud_palabra_ingresada("corazón",7)
    True
    >>> Validar_longitud_palabra_ingresada("zapato",5)
    False
    >>> Validar_longitud_palabra_ingresada("ballena",10)
    False
    >>> Validar_longitud_palabra_ingresada("supercalifragilisticoespialidoso",32)
    True
    >>> Validar_longitud_palabra_ingresada("1amarre",7)
    True
    >>> Validar_longitud_palabra_ingresada("*palabrota",10)
    True
    >>> Validar_longitud_palabra_ingresada("palabra de prueba",17)
    True
    >>> Validar_longitud_palabra_ingresada("* Ahora T0d0 Junto +",20)
    True
    """
    longitud_palabra = len(palabra)
    validador02 = longitud_palabra == longitud
    return validador02

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
        lista_aciertos_y_errores[posicion_lista_aciertos_y_errores] = " "
        posicion_lista_aciertos_y_errores += 1
    return lista_aciertos_y_errores

def Comparar_palabra_ingresada_con_respuesta(palabra,respuesta):
    """
    Esta funcion compara la palabra igresada por el jugador con la respuesta correcta del presente turno.
    Autor: Steven Guerrero
    """
    validacion = False
    if palabra == respuesta:
        validacion = True
    return validacion

def Seguir_jugando():
    """
    Esta función devuelve un valor booleano que sirve para verificar si el usuario quiere seguir jugando.
    Autor: Steven Guerrero
    """
    respuestas_positivas = ["SI","si","Si","sI","S","s","YES","Yes","yes","y","Y","true","True"]
    respuestas_negativas = ["No","NO","nO","n","N","false","False"]
    validacion = input("¿Desea seguir jugando? Escriba SI si desea seguir jugando, y escriba NO si desea salir:\n",)
    if validacion in respuestas_positivas:
        validacion = True
    elif validacion in respuestas_negativas:
        validacion = False
    #Falta agregar las excepciones
    return validacion

def Imprimir_resumen_de_juego(lista_letras, Lista_definiciones, lista_palabras_ingresadas, lista_aciertos_y_errores, posicion_turno):
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
    palabra_de_turno = Lista_definiciones[posicion_turno][SUBPOSICION_PALABRA_LISTA_DEFINICIONES]
    
    print("¡Ha concluido la partida!. Los resultados son:\n")
    for posicion_turno in range(0,len(lista_letras)):
        if lista_aciertos_y_errores[posicion_turno] == "a":
            print("Turno letra", lista_letras[posicion_turno], " - Palabra de ", len(palabra_de_turno)," letras - ", palabra_de_turno," - acierto")
        elif lista_aciertos_y_errores[posicion_turno] == "e":
            print("Turno letra", lista_letras[posicion_turno], " - Palabra de ", len(palabra_de_turno)," letras - ", lista_palabras_ingresadas[posicion_turno]," - error - Palabra Correcta: ", palabra_de_turno)
    return None

#ACA IRIA LA FUNCION DE SELECCION DE PALABRAS

def Diez_letras_ordenadas():
    """
    Esta función se encarga de seleccionar aleatoriamente las 10 palabras que se usaran en el rosco, junto con sus definiciones (ordenadas alfabeticamente).
    Autor: Facundo Cabral
    """
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z']
    random.shuffle(abecedario)
    diezletras = (sorted(abecedario[0:10]))
    if "ñ" in diezletras:
        for letra in diezletras:
            if letra == "ñ":
                letra = "ni"
        orddiezletras = sorted(diezletras)
        for letra in orddiezletras:
            if letra == "ni":
                letra = "ñ"
    return orddiezletras


def main():
    """
    Esta es la función principal. Se encarga de correr todas las demás funciones que componen el juego.
    Autor: Steven Guerrero
    """
    lista_letras = Diez_letras_ordenadas()
    Contador_aciertos = 0
    Contador_errores = 0
    puntaje = 0 #El jugador empieza con cero puntos su primera partida
    Validacion_seguir_jugando = True #Una variable de control para determinar si el jugador sigue jugando o desea terminar la partida.


    while Validacion_seguir_jugando:
        lista_palabras_ingresadas = [] #Una lista vacía que llevará registro de las palabras ingresadas por el jugador
        posicion_turno = 0 #Turno en el que se encuentra el jugador ne este momento. Empieza en cero.
        letra = lista_letras[posicion_turno] #Letra de la palabra a adivinar en este turno
        Lista_definiciones = Definiciones_para_el_rosco(DICCIONARIO,lista_letras) #"DICCIONARIO" Hace referencia al dicc. ordenado de la etapa 2
        palabra_de_turno = Lista_definiciones[posicion_turno][SUBPOSICION_PALABRA_LISTA_DEFINICIONES]
        longitud_palabra_de_turno = len(palabra_de_turno)
        definicion_de_turno = Lista_definiciones[posicion_turno][SUBPOSICION_DEFINICION_LISTA_DEFINICIONES]
        lista_aciertos_y_errores = Creacion_lista_vacia_aciertos_y_errores(lista_letras)
        
        while posicion_turno<len(lista_letras):
            print(lista_letras)
            print(lista_aciertos_y_errores, "\n")
            print("Aciertos: ", Contador_aciertos)
            print("Errores: ", Contador_errores)
            print("Turno letra ", letra, " - Palabra de ", longitud_palabra_de_turno, " letras")
            print("Definición: ", definicion_de_turno)
            palabra_ingresada = input("Ingrese palabra: ", )
            validacion01 = Validar_palabra_ingresada(palabra_ingresada)
            validacion02 = Validar_longitud_palabra_ingresada(palabra_ingresada,longitud_palabra_de_turno)
            while not validacion01 or not validacion02:
                print("Ingresó una palabra no válida.")
                print("La palabra no puede contener números, espacios ni ningún carácter especial y debe tener la misma cantidad de letras indicadas previamente junto a la letra de turno.")
                palabra_ingresada = input("Por favor ingrese una palabra válida para este turno: ", )
                validacion01 = Validar_palabra_ingresada(palabra_ingresada)
                validacion02 = Validar_longitud_palabra_ingresada(palabra_ingresada,longitud_palabra_de_turno)     
            if Comparar_palabra_ingresada_con_respuesta:
                Contador_aciertos += 1
                puntaje += 10 #Cada acierto suma 10ptos al jugador
                lista_aciertos_y_errores[posicion_turno] = "a"
                print("¡Correcto!\n")
            else:
                Contador_errores += 1
                puntaje -= 3 #Cada error resta 3 ptos al jugador
                lista_aciertos_y_errores[posicion_turno] = "e"
                print("¡Incorrecto! La respuesta correcta era: ", palabra_de_turno,"\n")
            lista_palabras_ingresadas.append(palabra_ingresada) #se agrega la palabra ingresada a una lista que lleva registro de las palabras ingresadas como respuestas por el usuario
            posicion_turno += 1
    
        Imprimir_resumen_de_juego(lista_letras, Lista_definiciones, lista_palabras_ingresadas, lista_aciertos_y_errores, posicion_turno)
        """
        Modulado en una funcion arriba:
        for posicion_turno in range(0,len(lista_letras)):
            if lista_aciertos_y_errores[posicion_turno] == "a":
                print("Turno letra", lista_letras[posicion_turno], " - Palabra de ", len(palabra_de_turno)," letras - ", palabra_de_turno," - acierto")
            elif lista_aciertos_y_errores[posicion_turno] == "e":
                print("Turno letra", lista_letras[posicion_turno], " - Palabra de ", len(palabra_de_turno)," letras - ", lista_palabras_ingresadas[posicion_turno]," - error - Palabra Correcta: ", palabra_de_turno)
        """
        print("Puntaje final: ", puntaje)
        Validacion_seguir_jugando = Seguir_jugando()
    return 0