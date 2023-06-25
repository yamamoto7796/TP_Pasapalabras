
def cargar_config_predeterminada(dicc_config_pred):
    """
    crea el archivo configuracion, con valores predeterminados
    Autor: Jonatan Misael Cruz
    """
    arch_config = open("configuracion.csv", "w")
    for elemento in dicc_config_pred:
        arch_config.write(elemento + "," + str(dicc_config_pred[elemento])+"\n")
    arch_config.close()

def ingresar_valor(posicion):
    """
    Solicita un valor a ingresar devolviendolo validado
    Autor: Jonatan Misael Cruz
    """
    valor = input()
    print()
    es_valido = False
    while not(es_valido):
        if valor.isalpha():
            print()
            valor = input("Valor invalido , debe ingresar un numero:  ")
            print()
        else:
            if posicion == 0 :
                if int(valor) >= 4 :
                    es_valido = True
                else :
                    valor = input("Valor invalido , debe ingresar un numero mayor o igual que '4':  ")
                    print()
            elif posicion == 1 :
                if 1<= int(valor) <= 27:
                    es_valido = True
                else:
                    valor = input("Valor invalido , debe ingresar un numero entre '1' y '27':  ")
                    print()
            elif posicion == 2 :
                if  int(valor) >= 1:
                    es_valido = True
                else:
                    valor = input("Valor invalido , debe ingresar un numero mayor o igual que '1':  ")
                    print()
            else :
                if int(valor) >= 0:
                    es_valido = True
                else:
                    valor = input("Valor invalido , debe ingresar un numero mayor o igual que '0':  ")
                    print()
    return valor
                
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
    dicc_configuraciones_predeterminadas = {"LONGITUD_PALABRA_MINIMA": 4,
                                            "CANTIDAD_LETRAS_ROSCO": 10,
                                            "MAXIMO_PARTIDAS": 5,
                                            "PUNTAJE_ACIERTO": 10,
                                            "PUNTAJE_DESACIERTO": 3}
    try:
        archivo_config = open("configuracion.csv")
        archivo_config.close()
    except FileNotFoundError:
        cargar_config_predeterminada(dicc_configuraciones_predeterminadas)
    respuesta = desea_cambiar_configuracion()
    if respuesta == "s":
        lista_elementos = ["LONGITUD_PALABRA_MINIMA",
                           "CANTIDAD_LETRAS_ROSCO",
                           "MAXIMO_PARTIDAS",
                           "PUNTAJE_ACIERTO",
                           "PUNTAJE_DESACIERTO"]
        lista_mensajes = ["Ingrese la longitud minima de cada palabra: ",
                      "Ingrese la cantidad de letras del rosco: ",
                      "Ingrese la cantidad maxima de partidas: ",
                      "Ingrese la cantidad de puntaje por acierto: ",
                      "Ingrese la cantidad de puntaje por desacierto: "]
        with open("configuracion.csv", "r+") as archivo_config:
                for posicion in range(len(lista_elementos)):
                    print(lista_mensajes[posicion], end="")
                    valor = ingresar_valor(posicion)
                    archivo_config.write(lista_elementos[posicion] + "," + str(valor) + "\n")


OMISION = "Omision"
CONFIG = "Configuracion"


def mostrar_configuraciones():
    """
    muestra por pantalla los valores de los elementos de la configuracion
    y si fueron obtenidos por omision o por configuracion.
    Autor: Jonatan Misael Cruz
    """
    lista_valores_defecto = [("LONGITUD_PALABRA_MINIMA", 4),
                             ("CANTIDAD_LETRAS_ROSCO", 10),
                             ("MAXIMO_PARTIDAS", 5),
                             ("PUNTAJE_ACIERTO", 10),
                             ("PUNTAJE_DESACIERTO", 3)]
    dicc_config = {}
    archivo_config = open('configuracion.csv')
    linea = archivo_config.readline()
    while linea:
        elemento, valor = linea.rstrip("\n").split(',')
        dicc_config[elemento] = valor
        linea = archivo_config.readline()
    archivo_config.close()
    dicc_estado_valores = {}
    for posicion in range(len(lista_valores_defecto)):
        if lista_valores_defecto[posicion][0] in dicc_config:
            dicc_estado_valores[lista_valores_defecto[posicion][0]] = [dicc_config[lista_valores_defecto[posicion][0]], CONFIG]
        else:
            dicc_estado_valores[lista_valores_defecto[posicion][0]] = [lista_valores_defecto[posicion][1], OMISION]
    print(f" ELEMENTO                  VALOR    ESTADO")
    print()
    for clave in dicc_estado_valores:
        print(f"{clave:25}    {dicc_estado_valores[clave][0]}   {dicc_estado_valores[clave][1]}")

