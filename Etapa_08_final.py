import random

def quitar_tilde(palabra):
    """
    Esta funcion quita la tilde de la palabra que la lleva

    Autor: Aaron Granda
    """
    vocales_con_tilde = ['á', 'é', 'í', 'ó', 'ú']
    vocales_sin_tilde = ['a', 'e', 'i', 'o', 'u']

    for i in range(len(vocales_con_tilde)):       
        palabra = palabra.replace(vocales_con_tilde[i], vocales_sin_tilde[i])
    
    return palabra

def generar_diccionario_de_palabras(archivo1, archivo2):
    """
    Esta funcion recibe dos archivos, 'palabras' y 'definiciones' donde cada palabra y su definicion se encuentran en la misma
    linea. cuando las recibe se va generado un diccionario cdando como clave 'palabra' y como valor su definicion.
    
    Autor: Aaron Granda
    """

    diccionario = {}

    with open(archivo1, "r", encoding= 'UTF-8') as palabras, open(archivo2, "r", encoding= 'UTF-8') as definiciones:
        linea_palabra = palabras.readline().rstrip('\n')
        linea_definicion = definiciones.readline().rstrip('\n')

        while (linea_palabra != "") and (linea_definicion != "") :
                linea_palabra_sin_tilde = quitar_tilde(linea_palabra)
                diccionario[linea_palabra_sin_tilde] = linea_definicion

                linea_palabra = palabras.readline().rstrip('\n')
                linea_definicion = definiciones.readline().rstrip('\n')

    return diccionario


def palabras_segun_longitud(diccionario, LONGITUD_PALABRA_MINIMA):
    """
    Esta funcion recibe el diccionario de palabras y definiciones y segun la longitud que indique el usuario se va
    generando el nuevo diccionario con la longitud especificada por el mismo usuario.

    Autor: Aaron Granda
    """

    diccionario_seleccion = {}
    for palabra, definicion in diccionario.items():
        if len(palabra) >= LONGITUD_PALABRA_MINIMA:
            diccionario_seleccion[palabra] = definicion
    return diccionario_seleccion


def ordenar_letras(lista):
    """
    Esta funcion ordena las letras del abecedario alfabeticamente.
    
    Autor: Aaron Granda
    """

    lista_ordenada = sorted(lista, key= lambda palabra: palabra.replace('ñ', 'n0'))
    return lista_ordenada


def seleccion_palabras_para_el_rosco(diccionario, CANTIDAD_LETRAS_ROSCO):
    """
    Esta funcion recibe el diccionario de la longitud especificada y lo que hace es escoger una palabra al azar
    por cada letra del abecedario random que se genere teniendo en cuenta la CANTIDAD DE LETRAS que se va
    a mostrar en el rosco y las guarda en un diccionario dando como clave la palabra y como valor su definicion.

    Autor: Aaron Granda
    """

    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                  'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    random.choice(alfabeto)
    cant_letras_al_azar = ordenar_letras(alfabeto[0:CANTIDAD_LETRAS_ROSCO])

    diccionario_resultado = {}
    for letra in cant_letras_al_azar:
        palabra_valida = False
        while not palabra_valida:
            par_seleccionado = random.choice(list(diccionario.items()))
            palabra_seleccionada = par_seleccionado[0]
            definicion_seleccionada = par_seleccionado[1]
            if palabra_seleccionada[0] == letra:
                palabra_valida = True
                diccionario_resultado[palabra_seleccionada] = definicion_seleccionada
    return diccionario_resultado


def mostrar_diccionario_candidato():
    """
    Esta funcion junta las funciones creadas anteriormente para presentar el diccionario final, y por ultimo
    va escribiendo en un archivo llamado 'diccionario.csv' las palabras elegidas con sus definiciones segun especifique 
    las condiciones el usuario (LONGITUD_PALABRA_MAXIMA, CANTIDAD_LETRAS_ROSCO) y luego cierra el archivo.
     
    Autor: Aaron Granda """

    
    diccionario = generar_diccionario_de_palabras('palabras.txt', 'definiciones.txt')
    diccionario_seleccion = palabras_segun_longitud(diccionario, 6) #LONGITUD_PALABRA_MINIMA
    diccionario_final = seleccion_palabras_para_el_rosco(diccionario_seleccion, 10) #CANT_LETRAS_ROSCO
    #print(diccionario_final)


    archivo_abierto = open('diccionario.csv', 'w', encoding= 'UTF-8')

    for palabra, definicion in diccionario_final.items():
        archivo_abierto.write(f"{palabra}, {definicion}\n")

    archivo_abierto.close()

    return 'diccionario.csv'

mostrar_diccionario_candidato()