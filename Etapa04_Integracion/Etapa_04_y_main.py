from Etapa_02 import obtener_diccionario
from Etapa_05 import comenzar_juego
from Etapa_01 import limpiar_pantalla
import random

def cargar_diccionario_de_palabras():
    """retorna el diccionario para ser usado en el juego
       autor: Jonatan misael cruz
    """
    diccionario = obtener_diccionario()
    print()
    continuar = input("Presione enter para continuar...")
    limpiar_pantalla()
    return diccionario

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
    #diccionario_palabras= obtener_diccionario()
    #mostrar_cant_palabras_y_cant_por_letra(diccionario_palabras)
    #limpiar_pantalla()
    diccionario_palabras = cargar_diccionario_de_palabras()#se obtiene de la etapa 2
    comenzar_juego(diccionario_palabras)                   #se obtiene de la etapa 5
    
main()