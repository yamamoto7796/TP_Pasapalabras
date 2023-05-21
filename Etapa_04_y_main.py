from Etapa_02 import obtener_diccionario
from Etapa_05 import comenzar_partida
from Etapa_01 import limpiar_pantalla
from Etapa_03 import Diez_letras_ordenadas, Definiciones_para_el_rosco
import random
import time

def mostrar_despedida_juego():
    """Muestra el mensaje de despedida del juego
    """
    print()
    print(f"************ ¡Gracias por jugar nuestro juego! **************")
    print()
    print(f"      ©Copyright 2023, Grupo MAGO. All Rights Reserved.")
    time.sleep(5)

def comenzar_juego(diccionario_palabras):
    """ Funcion que comienza el juego , iniciando las partidas que se jugaran
        Autor: Jonatan Misael Cruz
    """
    puntaje_final = 0
    sigue_jugando = True
    while sigue_jugando:
        lista_letras = Diez_letras_ordenadas()
        lista_definiciones = Definiciones_para_el_rosco(diccionario_palabras, lista_letras)
        sigue_jugando, puntaje_final = comenzar_partida(lista_letras, lista_definiciones, puntaje_final)
    limpiar_pantalla()
    mostrar_despedida_juego()
    
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
    continuar = input("Presione enter para continuar...")
    limpiar_pantalla()
    

def main():
    mostrar_bienvenida_juego()
    diccionario_palabras = obtener_diccionario()
    continuar = input("Presione enter para continuar...")
    limpiar_pantalla()
    comenzar_juego(diccionario_palabras)

main()

