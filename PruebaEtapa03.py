import random
from datos import *

DiccPrueba = obtener_lista_definiciones()
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z']
random.shuffle(abecedario)
lista_letras=sorted(abecedario[0:10])

def Definiciones_para_el_rosco(DiccionarioFiltrado,DiezLetras):
    """
    Esta función se encarga de seleccionar aleatoriamente las 10 letras que se usaran en el rosco.
    Autores: Facundo Cabral, José Adrián
    """
    # "DiezLetras" se define en el main, y es una lista al azar de 10 letras ordenadas alfabeticamente que se usaran para el juego.
    # "DiccionarioFiltrado" hace referencia al diccionario filtrado y aleatorizado obtenido de la etapa 2.
    Lista_definiciones =[]
    for letra in DiezLetras:
        palabra_valida = False
        while not palabra_valida:
            par_seleccionado = random.choice(DiccionarioFiltrado)
            pal_selec = par_seleccionado[0]
            def_selec = par_seleccionado[1]
            if pal_selec[0] == letra:
                palabra_valida = True
                Lista_definiciones.append([pal_selec,def_selec])
    return Lista_definiciones


for i in range(101):
    print(Definiciones_para_el_rosco(DiccPrueba,lista_letras))
    print("")

"""
    Podemos ver que la funcion en cada iteración selecciona palabras distintas para la misma letra,
    por ende, cumple con lo solicitado.
"""
