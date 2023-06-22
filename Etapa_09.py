
def Leer_Config():
    '''
    Funcion que leera el archivo "configuracion.csv" y definira los valores en variables constantes
    durante toda la partida.
    Autor: Facundo Cabral
    '''
    #Los valores por defecto definidos como constantes.
    LONG_PAL_MIN_DEF = 4
    CANT_LETRAS_ROSCO_DEF = 10
    MAX_PARTIDAS_DEF = 5
    PTS_ACIERTO_DEF = 10
    PTS_ERRORES_DEF = 3
    #Definimos las variables de tipo global para poder acceder a ellas fuera de esta funcion.
    global LONG_PALABRA_MIN,CANT_LETRAS_ROSCO,MAX_PARTIDAS,PUNTOS_ACIERTO,PUNTOS_ERRORES
    dicc_config = {}
    with open('configuracion.csv', 'r') as archivo_csv:
        linea = archivo_csv.readline()
        while linea:
            clave, valor = linea.strip().split(',')
            dicc_config[clave] = valor
            linea = archivo_csv.readline()
    #Los valores cargados del archivo CSV, estaran contenidos en el diccionario. Si algun valor
    #no posee ningun dato, se le asignara uno por defecto.
    LONG_PALABRA_MIN = int(dicc_config.get('LONGITUD_PALABRA_MINIMA', LONG_PAL_MIN_DEF))
    CANT_LETRAS_ROSCO = int(dicc_config.get('CANTIDAD_LETRAS_ROSCO', CANT_LETRAS_ROSCO_DEF))
    MAX_PARTIDAS = int(dicc_config.get('MAXIMO_PARTIDAS', MAX_PARTIDAS_DEF))
    PUNTOS_ACIERTO = int(dicc_config.get('PUNTAJE_ACIERTO', PTS_ACIERTO_DEF))
    PUNTOS_ERRORES = int(dicc_config.get('PUNTAJE_DESACIERTO', PTS_ERRORES_DEF))


# def main():
#     Leer_Config()
#     mostrar_bienvenida_juego()
#     input("Presione enter para continuar...")
#     limpiar_pantalla()
#     Comenzar_Juego()

# def Comenzar_Juego():
#     puntaje_final = Crear_Puntaje_Total() #Crea una lista con la cantidad de espacios = a jugadores
#     sigue_jugando = True
#     while sigue_jugando:
#         #Selecciona cada vez que se inicie la partida las letras y definiciones del rosco.
#         letras_seleccionadas,diccionario_final = mostrar_diccionario_candidato(LONG_PALABRA_MIN,CANT_LETRAS_ROSCO)
#         sigue_jugando, puntaje_final = Jugar_Partida(letras_seleccionadas,diccionario_final,puntaje_final)


def Crear_Puntaje_Total(Lista_Jugadores):
    '''
    Crea una lista con el numero total de jugadores y sus respectivos puntajes totales.
    Autor:Facundo Cabral
    '''
    puntaje_final = []
    for i in range(len(Lista_Jugadores)):
        puntaje_final.append(0)
    
    return puntaje_final

def Crear_Puntaje_Ronda(Lista_Jugadores):
    '''
    Crea una lista con el numero total de jugadores y sus respectivos puntajes de la ronda actual.
    Autor:Facundo Cabral
    '''
    puntaje_ronda = []
    for i in range(len(Lista_Jugadores)):
        puntaje_ronda.append(0)
    return puntaje_ronda

def Crear_Estadisticas(Lista_Jugadores):
    '''
    Esta funcion crea un contador para cada jugador en el cual se sumaran los errores y aciertos.
    Autor: Jose Adrian
    '''    
    estadisticas = {}
    for jugador in Lista_Jugadores:
        estadisticas[jugador] = {"Aciertos": 0, "Errores": 0}
    
    return estadisticas

def Crear_Lista_Turnos(letras_seleccionadas):
    '''
    Esta funcion crea el tablero donde se vera el turno actual del jugador.
    Autor:Facundo Cabral
    '''    
    lista_turnos = []
    for i in range(len(letras_seleccionadas)):
        lista_turnos.append(" ")
    return lista_turnos

# def Comenzar_Partida(letras_seleccionadas,diccionario_final,puntaje_final):
#     '''
#     Esta funcion determina el comienzo de cada partida. Los jugadores juegan con el mismo rosco
#     y definiciones hasta terminarlo. Luego eligen si jugar otro o terminar el juego.
    
#     Autor:Facundo Cabral
#     '''

# def MostrarTablero(letras_seleccionadas,lista_a_y_e,lista_turnos,estadisticas,letra_actual,long_palabra_actual,jugador_turno,definicion_de_turno):
#     """muestra el tablero por pantalla con las letras, las definiciones, los aciertos y errores
#        Autores: Jose Adrian     Colaborador: Facundo Cabral
#     """
#     print()
#     for posicion in range(len(letras_seleccionadas)):
#         print(f"[{letras_seleccionadas[posicion].upper()}]", end=" ")
#     for posicion in range(len(lista_turnos)):
#         print(f"[{lista_turnos[posicion]}]", end=" ")
#     for posicion in range(len(lista_a_y_e)):    
#         print(f"[{lista_a_y_e[posicion]}]", end=" ")
#     print()
#     print()
#     print("Jugadores")
#     for i, jugador in enumerate(Lista_Jugadores,1):
#         print(i, ".", jugador, "- Aciertos: ",estadisticas[jugador]["Aciertos"], "- Errores: ", estadisticas[jugador]["Errores"])
#     print("Turno Jugador", (jugador_turno+1), Lista_Jugadores[jugador_turno], "- Letra ", letra_actual(), " - Palabra de ", long_palabra_actual, " letras")
#     print("Definición: ", definicion_de_turno)

# def Actualizar_Datos(palabra_ingresada,palabra_actual,posicion_turno,jugador_turno,lista_a_y_e,estadisticas,puntaje_ronda):
#     '''
#     Esta funcion actualiza el puntaje de cada jugador luego de cada jugada.
    
#     Autor:Jose Adrian
#     '''
#     jugadoractual = Lista_Jugadores[jugador_turno]
#     if palabra_ingresada == palabra_actual:
#         lista_a_y_e[posicion_turno] = "a"
#         estadisticas[jugadoractual]["Aciertos"]+=PUNTOS_ACIERTO
#         puntaje_ronda[jugador_turno] +=PUNTOS_ACIERTO
#     else:
#         lista_a_y_e[posicion_turno] = "e"
#         estadisticas[jugadoractual]["Errores"]+=PUNTOS_ERRORES
#         puntaje_ronda[jugador_turno] -=PUNTOS_ERRORES
#         if jugador_turno == (len(Lista_Jugadores)-1):
#             jugador_turno = 0
#         else:
#             jugador_turno +=1
#     posicion_turno +=1

# def Actualizar_ListaTurnos(lista_turnos,posicion_turno,jugador_turno):
#     lista_turnos[posicion_turno] = jugador_turno


# def Jugar_Partida(letras_seleccionadas,diccionario_final,puntaje_final):
#     INDEX_POS_PALABRA = 0
#     INDEX_POS_DEFINICION = 1
#     puntaje_ronda = Crear_Puntaje_Ronda()
#     lista_turnos = Crear_Lista_Turnos(letras_seleccionadas)
#     estadisticas = Crear_Estadisticas()
#     lista_a_y_e = Crear_Lista_A_y_E(letras_seleccionadas)
#     posicion_turno = 0
#     jugador_turno = 0
#     palabras_y_definiciones = list(diccionario_final.items())
#     while posicion_turno < len(letras_seleccionadas):
#         Actualizar_ListaTurnos(lista_turnos,posicion_turno,jugador_turno)
#         palabra_actual = palabras_y_definiciones[posicion_turno][INDEX_POS_PALABRA]
#         definicion_actual = palabras_y_definiciones[posicion_turno][INDEX_POS_DEFINICION]
#         long_palabra_actual = len(palabra_actual)
#         letra_actual = letras_seleccionadas[posicion_turno]
#         MostrarTablero(letras_seleccionadas,lista_a_y_e,lista_turnos,estadisticas,letra_actual,long_palabra_actual,jugador_turno,definicion_actual)
#         palabra_ingresada = obtener_palabra(long_palabra_actual)
#         Actualizar_Datos(palabra_ingresada,palabra_actual,posicion_turno,jugador_turno,lista_a_y_e,estadisticas,puntaje_ronda)
