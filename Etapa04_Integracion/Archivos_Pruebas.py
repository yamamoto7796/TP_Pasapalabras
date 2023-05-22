from Etapa_02 import *

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
    validador02 = (longitud_palabra == longitud)
    return validador02

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

def Creacion_lista_vacia_aciertos_y_errores(lista_letras):
    """
    Esta función crea una lista vacía, la cual se va se usará como la lista inicial de de aciertos y errores con la que interactuará el jugador al iniciar el juego.
    Autor: Steven Guerrero
    >>> Creacion_lista_vacia_aciertos_y_errores(["A","B","C"])
    [' ', ' ', ' ']
    >>> Creacion_lista_vacia_aciertos_y_errores(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    >>> Creacion_lista_vacia_aciertos_y_errores(["A"])
    [' ']
    >>> Creacion_lista_vacia_aciertos_y_errores([" "])
    [' ']
    >>> Creacion_lista_vacia_aciertos_y_errores([])
    []
    >>> Creacion_lista_vacia_aciertos_y_errores(["A","B","C","D","E","F","G","H","I","J"])
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    """
    lista_aciertos_y_errores = []
    posicion_lista_aciertos_y_errores = 0
    while len(lista_aciertos_y_errores) < len(lista_letras):
        lista_aciertos_y_errores.append(" ")                #*aca tira un error "list assignment index out of range" , porque esta fuera del rango
        posicion_lista_aciertos_y_errores += 1              #le pongo un append para que se solucione 
    return lista_aciertos_y_errores

def Comparar_palabra_ingresada_con_respuesta(palabra,respuesta):
    """
    Esta funcion compara la palabra igresada por el jugador con la respuesta correcta del presente turno.
    Autor: Steven Guerrero
    >>> Comparar_palabra_ingresada_con_respuesta("palabra","respuesta")
    False
    >>> Comparar_palabra_ingresada_con_respuesta("respuesta","respuesta")
    True
    """
    validacion = False
    if palabra == respuesta:
        validacion = True
    return validacion

def quitar_tilde(diccionario_tilde):    #es la principal a ser llamada

    """Retorna un diccionario sacando las tildes de algunas palabras que la llevan en la clave.
    >>> quitar_tilde([['árbol', 's.m. BOTÁNICA. Planta de tronco leñoso que se ramifica a mayor o menor altura del suelo, formando una copa.']])
    {'arbol': 's.m. BOTÁNICA. Planta de tronco leñoso que se ramifica a mayor o menor altura del suelo, formando una copa.'}
    >>> quitar_tilde([['enigma', '1.  m. Enunciado de sentido artificiosamente encubierto para que sea difícil de entender o interpretar']])
    {'enigma': '1.  m. Enunciado de sentido artificiosamente encubierto para que sea difícil de entender o interpretar'}
    
    Autor: Aaron Granda"""

    # verificar si el usuario tiene que ingresar la palabra con acento
    lista_vocales_tildes = ['á', 'é', 'í', 'ó', 'ú']
    lista_vocales = ['a', 'e', 'i', 'o', 'u']

    diccionario_3 = seleccion_palabras_mayor_a_5(diccionario_tilde)
    diccionario_sin_tildes = {}

    for clave, valor in diccionario_3.items():      
        for num, vocal in enumerate(lista_vocales_tildes):
            if vocal in lista_vocales_tildes:
                clave = clave.replace(lista_vocales_tildes[num], lista_vocales[num])
        diccionario_sin_tildes[clave] = valor

    
    return diccionario_sin_tildes

#----------------------- Función doctest para Prueba------------------------#
import doctest
print(doctest.testmod())