
def Leer_Config():
    '''
    Funcion que leera el archivo "configuracion.csv" y definira los valores en variables constantes
    durante toda la partida.
    Autor: Jose Adrian
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

def Crear_Puntaje_Total(Lista_Jugadores):
    '''
    Crea una lista con el numero total de jugadores y sus respectivos puntajes totales.
    Autor:Jose Adrian
    '''
    puntaje_final = []
    for i in range(len(Lista_Jugadores)):
        puntaje_final.append(0)
    
    return puntaje_final

def Crear_Puntaje_Ronda(Lista_Jugadores):
    '''
    Crea una lista con el numero total de jugadores y sus respectivos puntajes de la ronda actual.
    Autor:Jose Adrian
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
    Autor:Jose Adrian
    '''    
    lista_turnos = []
    for i in range(len(letras_seleccionadas)):
        lista_turnos.append(" ")
    return lista_turnos