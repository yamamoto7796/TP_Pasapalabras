import random

#ACA IRIA LA FUNCION DE SELECCION DE PALABRAS
def Definiciones_para_el_rosco(DiccionarioFiltrado,DiezLetras):
    """
    Esta función se encarga de seleccionar aleatoriamente las 10 palabras que se usaran en el rosco, junto con sus definiciones (ordenadas alfabeticamente).
    Autor: José Adrián
    """
    # "DiezLetras" se define en la función "Diez_letras_ordenadas()", y es una lista al azar de 10 letras ordenadas alfabeticamente que se usaran para el juego.
    # "DiccionarioFiltrado" hace referencia al diccionario filtrado y aleatorizado obtenido de la etapa 2.
    Lista_definiciones =[] 
    for letra in DiezLetras:
        palabra_valida = False
        while not palabra_valida:
            par_seleccionado = random.choice(list(DiccionarioFiltrado.items()))#*le agregue el .items() por que daba error  de tipo de dato
            pal_selec = par_seleccionado[0]
            def_selec = par_seleccionado[1]
            if pal_selec[0] == letra:
                palabra_valida = True
                Lista_definiciones.append([pal_selec,def_selec])
    return Lista_definiciones

def Diez_letras_ordenadas():
    """
    Esta función se encarga de seleccionar aleatoriamente las 10 palabras que se usaran en el rosco, junto con sus definiciones (ordenadas alfabeticamente).
    Autor: Facundo Cabral
    """
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z']
    random.shuffle(abecedario)
    diezletras = (sorted(abecedario[0:10]))
    if "ñ" in diezletras: #Como la "ñ" es un caso excepcional y se ubica luego de la "z" en ASCII, procedemos a ordenarla.
        for letra in range(10):
            if diezletras[letra] == "ñ": #Si la letra actual es = "ñ", la cambiamos por "n0" temporalmente para poder ordenarla.
                diezletras[letra] = "n0"
        orddiezletras = sorted(diezletras) #La ordena nuevamente con las "n0"
        for letra in range(10):
            if orddiezletras[letra] == "n0": #Por ultimo, vuelve a convertir las "n0" en "ñ".
                orddiezletras[letra] = "ñ"
    else :                                  #agregue esto para que pueda devolver la lista en caso de que la ñ no este 
        orddiezletras = sorted(diezletras)  #es que sino daba un error "local variable 'orddiezletras' referenced before assignment"
    return orddiezletras                    #porque no estaba asignada la variable


