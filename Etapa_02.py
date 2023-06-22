from datos import obtener_lista_definiciones

def generar(lista):
    """Esta función convierte la lista 'definiciones' en un diccionario dando como clave la palabra y como valor su definición.
    
    Autor: Aaron Granda"""

    diccionario_lista = {}
    for elemento in lista:
        diccionario_lista[elemento[0]] = elemento[1]     
      
    return diccionario_lista


def seleccion_palabras_mayor_a_5(largo):
    """Esta función genera un diccionario nuevo con las palabras que son mayores o iguales a 5.
    
    Autor: Aaron Granda"""

    diccionario_2 = generar(largo) 
    diccionario_mayor_a_5 = {}
    for clave, valor in diccionario_2.items():
        if len(clave) >= 5:
            diccionario_mayor_a_5[clave] = valor

    return diccionario_mayor_a_5


def dicc_quitar_tilde(definiciones_con_tilde):    #es la principal a ser llamada

    """Retorna un diccionario sacando las tildes de algunas palabras que la llevan en la clave.
    >>> quitar_tilde({'árbol': s.m. BOTÁNICA. Planta de tronco leñoso que se ramifica a mayor o menor altura del suelo, formando una copa.})
    {'arbol': s.m. BOTÁNICA. Planta de tronco leñoso que se ramifica a mayor o menor altura del suelo, formando una copa.} 
    
    >>> quitar_tilde({'enigma': '1.  m. Enunciado de sentido artificiosamente encubierto para que sea difícil de entender o interpretar'})
    {'enigma': '1.  m. Enunciado de sentido artificiosamente encubierto para que sea difícil de entender o interpretar'}
    
    Autor: Aaron Granda"""


    lista_vocales_tildes = ['á', 'é', 'í', 'ó', 'ú']
    lista_vocales = ['a', 'e', 'i', 'o', 'u']

    diccionario_3 = seleccion_palabras_mayor_a_5(definiciones_con_tilde)
    diccionario_sin_tildes = {}

    for clave, valor in diccionario_3.items():      
        for num, vocal in enumerate(lista_vocales_tildes):
                
                clave = clave.replace(lista_vocales_tildes[num], lista_vocales[num])
        diccionario_sin_tildes[clave] = valor

    
    return diccionario_sin_tildes

def ordenar_por_clave(diccionario_candidato):
    """Esta función ordena el diccionario por orden alfabetico según las definiciones.
    
        
    Autor: Aaron Granda"""

    
    diccionario_4 = dicc_quitar_tilde(diccionario_candidato)
    diccionario_ordenado = dict(sorted(diccionario_4.items(), key= lambda x: x[0]))
    
    return diccionario_ordenado
        
#------------ comienzo de funciones para mostrar las cantidades de palabras por letra

def contador_palabras_totales(diccionario_final):
    """Esta función cuenta las palabras totales del diccionario.
    
    Autor: Aaron Granda"""

    
    contador_palabras = 0
    for clave in diccionario_final.keys():
        contador_palabras += 1
    return contador_palabras


def contador_por_letra(diccionario_final_2):
    """Esta función cuenta cuantas palabras hay por cada letra del alfabeto.
    
    Autor: Aaron Granda"""

    dicc_cont_letras = {}
    for clave in diccionario_final_2.keys():
        if clave[0] in dicc_cont_letras:
            dicc_cont_letras[clave[0]] += 1
        else:
            dicc_cont_letras[clave[0]] = 1
    return dicc_cont_letras

def imprimir_total_por_letra(diccionario_por_letra):
    """Esta función imprime cuantas palabras hay por cada letra del afabeto.
    
    Autor: Aaron Granda"""
    
    diccionario_impreso = contador_por_letra(diccionario_por_letra)
    for letra in diccionario_impreso:
        print(f"Letra: '{letra}' - Cantidad de palabras: {diccionario_impreso[letra]}")
   


def obtener_diccionario():
    """Esta es una funcion que retorna un diccionario de palabras obtenido de la lista de definiciones y muestra las 
    cantidades de palabras que hay.
    
        Autor: Aaron Granda
    """    
    definiciones = obtener_lista_definiciones()
    diccionario_palabras = ordenar_por_clave(definiciones)
    print()
    print(f"Palabras en total: {contador_palabras_totales(diccionario_palabras)}.")
    print()
    imprimir_total_por_letra(diccionario_palabras)
    print()
    return diccionario_palabras

