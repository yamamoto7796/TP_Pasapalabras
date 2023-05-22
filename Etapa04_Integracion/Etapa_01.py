import os

SUBPOSICION_PALABRA_LISTA_DEFINICIONES = 0 #posición de la palabra de turno en el array de palabras y definiciones
SUBPOSICION_DEFINICION_LISTA_DEFINICIONES = 1 #posición de la definición de turno en el array de palabras y definiciones


def limpiar_pantalla():
    """genera la limpieza de la pantalla
       Autor: Jonatan Cruz
    """
    if os.name == "posix":
        os.system("clear")
    elif os.name in ("ce", "nt", "dos"):
        os.system("cls")
        

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



def Comparar_palabra_ingresada_con_respuesta(palabra,respuesta):
    """
    Esta funcion compara la palabra igresada por el jugador con la respuesta correcta del presente turno.
    Autor: Steven Guerrero
    """
    validacion = False
    if palabra == respuesta:
        validacion = True
    return validacion

def hay_aciertos_o_errores(palabra_de_turno, palabra_ingresada, posicion_turno, Contador_aciertos, Contador_errores, lista_aciertos_y_errores):
    """Funcion que determina si hubo aciertos o errores, retornandolos
       Autor: Steven Guerrero
    """
    if Comparar_palabra_ingresada_con_respuesta(palabra_de_turno, palabra_ingresada):
        Contador_aciertos += 1
        lista_aciertos_y_errores[posicion_turno] = "a"
        print("¡Correcto!\n")
    else:
        Contador_errores += 1
        lista_aciertos_y_errores[posicion_turno] = "e"
        print("¡Incorrecto! La respuesta correcta era: ", palabra_de_turno,"\n")
    return Contador_aciertos, Contador_errores

def obtener_palabra(longitud_palabra_de_turno):
    """funcion que obtiene una palabra y la retorna validada
       Autor: Steven Guerrero   
    """
    palabra_ingresada = input("Ingrese palabra: ", )
    validacion01 = Validar_palabra_ingresada(palabra_ingresada)
    validacion02 = Validar_longitud_palabra_ingresada(palabra_ingresada,longitud_palabra_de_turno)
    while not validacion01 or not validacion02:
        print()
        print("Ingresó una palabra no válida.")
        print("La palabra no puede contener números, espacios ni ningún carácter especial y debe tener la misma cantidad de letras indicadas previamente junto a la letra de turno.")
        print()
        palabra_ingresada = input("Por favor ingrese una palabra válida para este turno: ", )
        validacion01 = Validar_palabra_ingresada(palabra_ingresada)
        validacion02 = Validar_longitud_palabra_ingresada(palabra_ingresada,longitud_palabra_de_turno)
    return palabra_ingresada

def mostrar_tablero(lista_letras, lista_aciertos_y_errores, Contador_aciertos, Contador_errores, letra, longitud_palabra_de_turno, definicion_de_turno):
    """muestra el tablero por pantalla con las letras, las definiciones, los aciertos y errores
       Autor: Steven Guerrero       , Colaboracion: Jonatan Cruz
    """
    print()
    for posicion in range(len(lista_letras)):
        print(f"[{lista_letras[posicion].upper()}]", end=" ")
    print()
    for posicion in range(len(lista_aciertos_y_errores)):    
        print(f"[{lista_aciertos_y_errores[posicion]}]", end=" ")
    print()
    print()
    print()
    print("Aciertos: ", Contador_aciertos)
    print("Errores: ", Contador_errores)
    print("Turno letra ", letra.upper(), " - Palabra de ", longitud_palabra_de_turno, " letras")
    print("Definición: ", definicion_de_turno)
        

def jugar(lista_letras, lista_aciertos_y_errores,lista_palabras_ingresadas, Lista_definiciones, Contador_aciertos,Contador_errores, posicion_turno):
    """Funcion que realiza las jugadas de cada partida , retornando los errores y aciertos que se obtuvieron
       Autor: Steven Guerrero , Colaboracion: Jonatan Cruz
    """
    
    while posicion_turno<len(lista_letras):
        palabra_de_turno = Lista_definiciones[posicion_turno][SUBPOSICION_PALABRA_LISTA_DEFINICIONES]
        longitud_palabra_de_turno = len(palabra_de_turno)
        letra = lista_letras[posicion_turno]
        definicion_de_turno = Lista_definiciones[posicion_turno][SUBPOSICION_DEFINICION_LISTA_DEFINICIONES]
        mostrar_tablero(lista_letras, lista_aciertos_y_errores,Contador_aciertos, Contador_errores, letra, longitud_palabra_de_turno, definicion_de_turno)
        palabra_ingresada = obtener_palabra(longitud_palabra_de_turno)
        limpiar_pantalla()
        Contador_aciertos, Contador_errores = hay_aciertos_o_errores(palabra_de_turno, palabra_ingresada, posicion_turno, Contador_aciertos, Contador_errores, lista_aciertos_y_errores)
        lista_palabras_ingresadas.append(palabra_ingresada) #se agrega la palabra ingresada a una lista que lleva registro de las palabras ingresadas como respuestas por el usuario
        posicion_turno += 1
    return Contador_aciertos, Contador_errores
