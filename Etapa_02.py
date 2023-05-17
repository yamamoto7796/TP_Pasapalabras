from datos import obtener_lista_definiciones
definiciones = obtener_lista_definiciones()


def generar_diccionario(lista):
    """Esta función convierte la lista 'definiciones' en un diccionario dando como clave la palabra y como valor su definición.
    
    Autor: Aaron Granda"""

    diccionario_lista = {}
    for elemento in lista:
        diccionario_lista[elemento[0]] = elemento[1]     
      
    return diccionario_lista


def seleccion_palabras_mayor_a_5(diccionario_seleccion):
    """Esta función genera un diccionario nuevo con sacando a las palabras que tienen 4 o menos letras totales.
    
    Autor: Aaron Granda"""

    diccionario_2 = generar_diccionario(diccionario_seleccion)
    diccionario_mayor_a_5 = {}
    for clave, valor in diccionario_2.items():
        if len(clave) >= 5:
            diccionario_mayor_a_5[clave] = valor

    return diccionario_mayor_a_5


def quitar_tilde(diccionario_tilde):

    """Retorna un diccionario sacando las tildes de algunas palabras que la llevan en la clave.
    >>> quitar_tilde({'árbol': s.m. BOTÁNICA. Planta de tronco leñoso que se ramifica a mayor o menor altura del suelo, formando una copa.})
    {'arbol': s.m. BOTÁNICA. Planta de tronco leñoso que se ramifica a mayor o menor altura del suelo, formando una copa.} 
    
    >>> quitar_tilde({'enigma': '1.  m. Enunciado de sentido artificiosamente encubierto para que sea difícil de entender o interpretar'})
    {'enigma': '1.  m. Enunciado de sentido artificiosamente encubierto para que sea difícil de entender o interpretar'}
    
    Autor: Aaron Granda"""

    # verificar si el usuario tiene que ingresar la apabra con acento
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
        

def contador_palabras_totales_diccionario(diccionario_final):
    """Esta función cuenta las palabras totales del diccionario.
    
    Autor: Aaron Granda"""

    diccionario_4 = quitar_tilde(diccionario_final)
    contador_palabras = 0
    for clave in diccionario_4.keys():
        contador_palabras += 1
    return contador_palabras


def contador_por_letra(diccionario_final_3):
    """Esta función cuenta cuantas palabras hay por cada letra del abecedario.
    
    Autor: Aaron Granda"""

    diccionario_4 = quitar_tilde(diccionario_final_3)
    dicc_letras = {}
    for clave in diccionario_4.keys():
        if clave[0] in dicc_letras:
            dicc_letras[clave[0]] += 1
        else:
            dicc_letras[clave[0]] = 1
    
    dicc_ordenado_letras = sorted(dicc_letras)
    for clave in dicc_ordenado_letras:
        print(f"Letra '{clave}': Cantidad de palabras: {dicc_letras[clave]}")


print(quitar_tilde(definiciones))
print(f"Palabras en total: {contador_palabras_totales_diccionario(definiciones)}.")
print(contador_por_letra(definiciones))



