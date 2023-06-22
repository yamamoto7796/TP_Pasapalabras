'''
def cargar_config_predeterminada(dicc_config_pred):
    """
    crea el archivo configuracion, con valores predeterminados
    Autor: Jonatan Misael Cruz
    """
    arch_config = open("configuracion.csv", "w")
    for elemento in dicc_config_pred:
        arch_config.write(elemento + "," + str(dicc_config_pred[elemento])+"\n")
    arch_config.close()
'''

def ingresar_valor():
    """
    Solicita un valor a ingresar devolviendolo validado
    Autor: Jonatan Misael Cruz
    """
    valor = input()
    es_valido = False
    while not(es_valido):
        if not(valor.isdigit()):
            print()
            valor = input("Valor invalido , debe ingresar un numero:  ")
        else:
            es_valido = True
    return valor

def leer_linea(archivo_config):
    """
    Realiza la lectura de cada linea del archivo, devolviendo la secuencia de datos obtenido
    Autor: Jonatan Misael Cruz
    """
    linea = archivo_config.readline()
    datos = linea.rstrip("\n").split(",")
    return datos


def ingreso_nuevos_valores_configuracion(lista_elementos_valores, archivo_config):
    """
    Solicita el ingreso de nuevos valores en la configuracion
    Autor: Jonatan Misael Cruz
    """
    lista_mensajes = ["Ingrese la longitud minima de cada palabra: ",
                      "Ingrese la cantidad de letras del rosco: ",
                      "Ingrese la cantidad maxima de partidas: ",
                      "Ingrese la cantidad de puntaje por acierto: ",
                      "Ingrese la cantidad de puntaje por desacierto: "]
    for mensaje in lista_mensajes:
        print()
        elemento, valor = leer_linea(archivo_config)
        print(mensaje, end="")
        valor = ingresar_valor()
        lista_elementos_valores.append((elemento, int(valor)))
        
        
def desea_cambiar_configuracion():
    """
    Obtiene una respuesta y la valida, para poder realizar modificaciones en la
    configuracion.
    Autor: Jonatan Misael Cruz
    """
    respuesta = input("¿Desea cambiar las configuraciones del juego?, s/n . (s = si) , (n = no): ")
    es_valida = False
    while not(es_valida):
        if respuesta != "s" and respuesta != "n":
            respuesta = input("Debe ingresar la letra ' s ' o la letra ' n ', (s = si) , (n = no): ")
        else:
            es_valida = True
    return respuesta


def configuracion():
    """
    funcion que crea el archivo de configuraciones y en caso de ser solicitado,
    realiza las modificaciones.
    Autor: Jonatan Misael Cruz
    """
    '''
    dicc_configuraciones_predeterminadas = {"LONGITUD_PALABRA_MINIMA": 4,
                                            "CANTIDAD_LETRAS_ROSCO": 10,
                                            "MAXIMO_PARTIDAS": 5,
                                            "PUNTAJE_ACIERTO": 10,
                                            "PUNTAJE_DESACIERTO": 3}
    cargar_config_predeterminada(dicc_configuraciones_predeterminadas)
    '''
    respuesta = desea_cambiar_configuracion()
    if respuesta == "s":
        lista_elementos_valores = []
        with open("configuracion.csv", "r+") as archivo_config:
                ingreso_nuevos_valores_configuracion(lista_elementos_valores, archivo_config)
                archivo_config.seek(0)
                for elemento in lista_elementos_valores:
                    archivo_config.write(elemento[0] + "," + str(elemento[1]) + "\n")


