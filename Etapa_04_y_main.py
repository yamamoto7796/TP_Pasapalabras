from Etapa_05 import *
from Etapa_01 import limpiar_pantalla
from Etapa_08_final import *
import Etapa_09
import Etapa_07
import random
import time

def mostrar_despedida_juego():
    """Muestra el mensaje de despedida del juego
       Autor: Jonatan Misael Cruz
    """
    print()
    print(f"************ ¡Gracias por jugar nuestro juego! **************")
    print()
    print(f"      ©Copyright 2023, Grupo MAGO. All Rights Reserved.")
    time.sleep(5)

def comenzar_juego():
    """ Funcion que comienza el juego , iniciando las partidas que se jugaran
        Autor: Jonatan Misael Cruz
    """
    puntaje_final = Etapa_09.Crear_Puntaje_Total(Etapa_07.Lista_Jugadores) #Crea una lista con la cantidad de espacios = a jugadores
    sigue_jugando = True
    contador = 1
    while sigue_jugando:

        lista_letras,lista_definiciones = mostrar_diccionario_candidato(Etapa_09.LONG_PALABRA_MIN,Etapa_09.CANT_LETRAS_ROSCO)
        sigue_jugando, puntaje_final, contador = comenzar_partida(lista_letras, lista_definiciones, puntaje_final,contador)
        limpiar_pantalla()
    
def mostrar_bienvenida_juego():
    """muestra el mensaje de inicio y los nombres de los integrantes del grupo
       autor: Jonatan Misael Cruz
    """
    print(f"********** Bienvenido al juego pasapalabra del grupo MAGO ********** ")
    print()
    print(f"Integrantes : JOSE ADRIAN")
    print(f"              FACUNDO MAXIMILIANO CABRAL")
    print(f"              STEVEN ANTONIO JOSE GERRERO LARA")
    print(f"              AARON JOSE GRANDA DORIA")
    print(f"              JONATAN MISAEL CRUZ")
    print()
    lista_frases = ['"Las palabras son como monedas,@ que una vale por muchas como muchas no valen por una. "',
                    '"Las palabras elegantes no son sinceras;@ las palabras sinceras no son elegantes. "',
                    '"A menudo me he tenido que comer mis palabras@ y he descubierto que eran una dieta equilibrada. "',
                    '" —¿Qué vas a hacer, boa? —preguntó el cazador.@ -Te BOA morder "',
                    '"Repite conmigo: Hakuna Matata...@Esas dos palabras resolverán todos tus problemas."']
    print(f"{'*'*60}")
    print()
    frase = random.choice(lista_frases)
    frase_partida = frase.split("@")
    for mitad_frase in frase_partida:
        print(f"     {mitad_frase:>20s}")
    print()
    print(f"{'*'*60}")
    print()
    input("Presione enter para continuar...")
    limpiar_pantalla()
    

def IniciarGame():
    Etapa_07.crear_ventana()
    Etapa_09.Leer_Config()
    mostrar_bienvenida_juego()
    input("Presione enter para continuar...")
    limpiar_pantalla()
    comenzar_juego()
    mostrar_despedida_juego()

IniciarGame()