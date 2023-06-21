import random

def leer_archivo_por_linea(linea):

    campo = linea.readline().rstrip('\n')
    return campo


def quitar_tilde(palabra):
    vocales_con_tilde = ['á', 'é', 'í', 'ó', 'ú']
    vocales_sin_tilde = ['a', 'e', 'i', 'o', 'u']

    for i in range(len(vocales_con_tilde)):       
        palabra = palabra.replace(vocales_con_tilde[i], vocales_sin_tilde[i])
    
    return palabra


def generar_diccionario_de_palabras(archivo1, archivo2):
    diccionario = {}

    with open(archivo1, 'r', encoding= 'UTF-8') as palabras, open(archivo2, 'r', encoding= 'UTF-8') as definiciones:
        linea_palabra = leer_archivo_por_linea(palabras)
        linea_palabra_sin_tilde = quitar_tilde(linea_palabra)

        linea_definicion = leer_archivo_por_linea(definiciones)

        while linea_palabra and linea_definicion:
            diccionario[linea_palabra_sin_tilde] = linea_definicion

            linea_palabra = leer_archivo_por_linea(palabras)
            linea_palabra_sin_tilde = quitar_tilde(linea_palabra)

            linea_definicion = leer_archivo_por_linea(definiciones)

    return (diccionario)


def ordenar_letras(lista):
    lista_ordenada = sorted(lista, key= lambda palabra: palabra.replace('ñ', 'n0'))
    return lista_ordenada


def diccionario_longitud_admitida(diccionario, LONGITUD_MINIMA):
    dicc_result = {}
    for palabra, definicion in diccionario.items():
        if len(palabra) >= LONGITUD_MINIMA:
            dicc_result[palabra] = definicion

    return dicc_result


def seleccion_de_letras_al_azar(abecedario, CANTIDAD_LETRAS_ROSCO):
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                  'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    random.shuffle(abecedario)
    letras_al_azar = abecedario[0: CANTIDAD_LETRAS_ROSCO]

    return ordenar_letras(letras_al_azar)


def seleccionar_palabras_al_azar(diccionario, CANTIDAD_LETRAS_ROSCO):
    """
    """
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                  'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    random.shuffle(abecedario)
    letras_al_azar = abecedario[0: CANTIDAD_LETRAS_ROSCO]
    letras_al_azar_ordenadas = ordenar_letras(letras_al_azar)

    diccionario_filtrado = {}
    for letra in letras_al_azar_ordenadas:
        palabra_valida = False
        while not palabra_valida:
            par_seleccionado = random.choice(list(diccionario.items()))
            palabra_seleccionada = par_seleccionado[0]
            definicion_seleccionada = par_seleccionado[1]
            if palabra_seleccionada[0] == letra:
                palabra_valida = True
                diccionario_filtrado[palabra_seleccionada] = definicion_seleccionada

    return diccionario_filtrado


def obtener_diccionario_palabras_candidatas():
    diccionario_archivo = generar_diccionario_de_palabras('palabras.txt', 'definiciones.txt')
    
    resultado = diccionario_longitud_admitida(diccionario_archivo, 8)
    palabras_para_el_rosco = seleccionar_palabras_al_azar(resultado, 8)
    print(palabras_para_el_rosco)
    

obtener_diccionario_palabras_candidatas()








