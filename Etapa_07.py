from tkinter import *
from tkinter import messagebox
import random
#import Etapa_04_y_main

#Constantes
USUARIO = 0
CLAVE = 1
USUARIO_CORTE = "0000000000"
CLAVE_CORTE = "000000"
CONDICION_CORTE_REGISTRO = USUARIO_CORTE + "," + CLAVE_CORTE
MAXIMO_JUGADORES = 4
MAXIMO_CARACTERES_USUARIO = 20
MINIMO_CARACTERES_USUARIO = 4
MAXIMO_CARACTERES_CLAVE = 12
MINIMO_CARACTERES_CLAVE = 6

#Mensajes de error o advertencia que pueden aparecer según los botones que presione usuario
#Autor de todos estos mensajes de error e información: Steven Guerrero

def LoginIncorrecto():
    messagebox.showerror("Error de inicio de sesión", "El usuario o clave estan incorrectos")

def ClavesIncorrectas():
    messagebox.showerror("Error de inicio de sesión", "Las contraseñas introducidas no coinciden")
    
def LoginCorrecto():
    messagebox.showinfo("Login correcto", "Usuario y Clave correctos.\nJugador agregado a la partida")
    
def UsuarioExistente():
    messagebox.showerror("Error de inicio de sesión", "Este usuario ya existe")

def UsuarioAgregado():
    messagebox.showerror("Error de inicio de sesión", "Este usuario ya forma parte de esta partida")

def MaximoJugadoresAlcanzado():
    messagebox.showinfo("Login correcto", "Usuario y Clave correctos\nJugador agregado a la partida\nMáximo de Jugadores alcanzado, se iniciará partida")

def UsuarioIncorrecto():
    messagebox.showerror("Error de registro de usuario", "El usuario introducido tiene más de 20 caracteres o menos de 4 caracteres\no posee un caracter no valido.\nSolo se permiten letras, números y el guión medio (-)")

def ClaveIncorrecta():
    messagebox.showerror("Error de registro de usuario", "La contraseña introducida no es válida.\nDebe tener una longitud entre 6 y 12 caracteres.\nDebe contener al menos una letra mayúscula, una letra minúscula, un número y alguno de los siguientes caracteres especiales: ! #\nNo se puede usar un caracter diferente a los ya mencionados.")

def Mensaje_Error_Iniciar_Partida():
    messagebox.showerror("Error de registro de usuario", "Tiene que ingresar al menos un jugador para poder iniciar partida")

#Validaciones de usuario y clave

def Validar_Usuario(Usuario01, Registro_Usuarios_Claves):
    """Esta funcion se encarga de verificar que el usuario introducido es válido.
    Para que sea válido debe cumplir con la longitud permitida y tener caracteres válidos.
    Autor: Steven Guerrero
    Args:
        Usuario01 (string): El nombre de usuario introducido
        Registro_Usuarios_Claves (diccionario): Diccionario con los usuarios existentes y sus respectivas claves.

    Returns:
        Cantidad de errores dentro del nombre de usuario (int)
        
    Pruebas unitarias:
    >>> Validar_Usuario("Steven",{"Usuario":"Hola123!"})
    0
    >>> Validar_Usuario("Steven",{"Steven":"Hola123!"})
    1
    >>> Validar_Usuario("Steven!",{"Usuario":"Hola123!"})
    1
    >>> Validar_Usuario("Steven-7",{"Usuario":"Hola123!"})
    0
    >>> Validar_Usuario("ST",{"Usuario":"Hola123!"})
    1
    >>> Validar_Usuario("EstoEsUnUsuarioMuyLargo",{"Usuario":"Hola123!"})
    1
    >>> Validar_Usuario("12345",{"Usuario":"Hola123!"})
    0
    >>> Validar_Usuario("1234-5",{"Usuario":"Hola123!"})
    0
    >>> Validar_Usuario("----",{"Usuario":"Hola123!"})
    0
    >>> Validar_Usuario("12345",{"12345":"Hola123!"})
    1
    """
    Contador_Errores = 0
    Contador = 0
    Caracteres_validos = ["á","é","í","ó","ú","ñ"]
    if Usuario01 in Registro_Usuarios_Claves.keys():
            Contador_Errores += 1
            UsuarioExistente()
    elif len(Usuario01)<=MAXIMO_CARACTERES_USUARIO and len(Usuario01)>= MINIMO_CARACTERES_USUARIO:
        while Contador < len(Usuario01) and Contador_Errores == 0:
            if not ((Usuario01[Contador].isalnum()) or (Usuario01[Contador] == "-") or (Usuario01[Contador] in Caracteres_validos)):
                Contador_Errores += 1 #Preguntar si debe obligatoriamente tener los tres tipos de caracteres o si lo importante es que no contenga alguno distintos a estos.
            Contador += 1
        if Contador_Errores != 0:
            UsuarioIncorrecto()
    else:
        Contador_Errores += 1
        UsuarioIncorrecto()
    return Contador_Errores

def Validar_Clave(Clave01):
    """Esta funcion se encarga de verificar que la clave introducida es válida.
    Para que sea válida debe cumplir con la longitud permitida y tener al menos uno de cada caracter válido.
    Autor: Steven Guerrero
    Args:
        Clave01 (string): La clave introducida

    Returns:
        Cantidad de errores dentro de la clave (int)
    >>> Validar_Clave("Hola123!")
    0
    >>> Validar_Clave("Hola")
    1
    >>> Validar_Clave("Hola.123")
    2
    >>> Validar_Clave("EstoesunaclaveMuyLarga123!")
    1
    >>> Validar_Clave("Hola1234")
    1
    >>> Validar_Clave("Hola!#!#!")
    1
    >>> Validar_Clave("hola123!")
    1
    >>> Validar_Clave("HOLA123!")
    1
    >>> Validar_Clave("1234567!")
    1
    >>> Validar_Clave("!!!!!!!!")
    1
    >>> Validar_Clave("123456789")
    1
    >>> Validar_Clave("HolaValido")
    1
    """
    Contador_Errores = 0
    Contador = 0
    Contador_Mayusculas = 0
    Contador_Minusculas = 0
    Contador_Numeros = 0
    Contador_Caracter_Especial = 0
    Caracteres_especiales = ["!","#"]
    if len(Clave01)<=MAXIMO_CARACTERES_CLAVE and len(Clave01)>= MINIMO_CARACTERES_CLAVE:
        while Contador < len(Clave01) and Contador_Errores == 0:
            if Clave01[Contador] == Clave01[Contador].upper() and Clave01[Contador].isalpha():
                Contador_Mayusculas += 1
            elif Clave01[Contador] == Clave01[Contador].lower() and Clave01[Contador].isalpha():
                Contador_Minusculas += 1
            elif Clave01[Contador].isnumeric():
                Contador_Numeros += 1
            elif Clave01[Contador] in Caracteres_especiales:
                Contador_Caracter_Especial += 1
            else:
                Contador_Errores += 1
            Contador += 1
        if (Contador_Errores != 0 or Contador_Caracter_Especial<1 or Contador_Mayusculas<1 or Contador_Minusculas<1 or Contador_Numeros<1):
            Contador_Errores += 1
            ClaveIncorrecta()
    else:
        Contador_Errores += 1
        ClaveIncorrecta()
    return Contador_Errores

#Funciones asociadas a trabajar con archivos

def Leer_Lineas_de_Usuarios(archivo):
    """Esta función lee una línea de un archivo convirtiéndola en una lista.
    Autor: Steven Guerrero
    Args:
        archivo (file): Un archivo .csv

    Returns:
        linea (list): Una lista compuesta por los valores del archivo .csv
    >>> archivo = open("usuarios.csv","r+")
    >>> Leer_Lineas_de_Usuarios(archivo)
    ['Facu', 'Hola123!']
    >>> archivo.close()
    """
    linea = archivo.readline()
    if (not(linea)):
        linea = CONDICION_CORTE_REGISTRO
    linea = linea.rstrip()
    return linea.split(',')

def Crear_Diccionarios_Usuarios(archivo):
    """Esta función lee una línea de un archivo convirtiéndola en una lista.
    Autor: Steven Guerrero
    Args:
        archivo (file): Un archivo .csv

    Returns:
        Registro_Usuarios_Claves (diccionario): Diccionario conlos usuarios ya previamente registrados como claves y sus contrasenas como valores.
    
    >>> archivo = open("usuarios.csv","r+")
    >>> Crear_Diccionarios_Usuarios(archivo)
    {'Facu': 'Hola123!', 'Jose': 'Hola123!', 'Steven': 'Hola123!'}
    >>> archivo.close()   
    """
    Registro_Usuarios_Claves = {}
    Usuario_Clave =["",""]
    while (Usuario_Clave[USUARIO] != USUARIO_CORTE and Usuario_Clave[CLAVE] != CLAVE_CORTE):
        Usuario_Clave = Leer_Lineas_de_Usuarios(archivo)
        if (Usuario_Clave[USUARIO] != USUARIO_CORTE and Usuario_Clave[CLAVE] != CLAVE_CORTE): #Verificar si hay alguna manera de  no necesitar esta verificacion y que no agregue la condicion de corte al diccionario.
            Registro_Usuarios_Claves[Usuario_Clave[USUARIO]] = Usuario_Clave[CLAVE]
    return Registro_Usuarios_Claves


#Funciones asociadas a los botones de la interfaz

def Iniciar_Partida():
    """ Esta función permite que pueda empezarl el juego de Pasapalabras.
    Para empezar el juego verifica que haya al menos un jugador introducido y vuelve aleatorio el orden de jugadores introducidos.
    Finalmente cierra la ventana.
    Autor: Steven Guerrero
    """
    if Lista_Jugadores == []:
        Mensaje_Error_Iniciar_Partida()
    else:
        random.shuffle(Lista_Jugadores)
        ventana.destroy()

def Ingresar_usuario(Registro_Usuarios_Claves): 
    """Esta función agrega el usuario introducido a la partida. Esto lo hace agregando a la lista "Lista_Jugadores" que es una variable global.
    Autor: Steven Guerrero
    
    Args:
        Registro_Usuarios_Claves (diccionario): Diccionario conlos usuarios ya previamente registrados como claves y sus contrasenas como valores.
    """
    Usuario01 = Verificar_jugador.get()
    Clave01 = Verificar_primera_clave.get()
    Clave02 = Verificar_segunda_clave.get()
    if Clave01 != Clave02:
        ClavesIncorrectas()
    else:
        if Usuario01 in Lista_Jugadores:
            UsuarioAgregado()
        elif Usuario01 in Registro_Usuarios_Claves.keys() and Clave01 == Registro_Usuarios_Claves[Usuario01]:
            Lista_Jugadores.append(Usuario01)
            if len(Lista_Jugadores) == MAXIMO_JUGADORES: #Una vez alcanzado el máximo de jugadores, la función llama a "Iniciar_partida" para comenzar el juego y cerrar la ventana.
                MaximoJugadoresAlcanzado()
                Iniciar_Partida()
            else:
                LoginCorrecto()
        else:
            LoginIncorrecto()
        
def Registrar_usuario(Registro_Usuarios_Claves):
    """Esta función agrega el usuario introducido tanto al archivo .csv como a la partida.
    Autor: Steven Guerrero
    
    Args:
        Registro_Usuarios_Claves (diccionario): Diccionario conlos usuarios ya previamente registrados como claves y sus contrasenas como valores.
    """
    Usuario01 = Verificar_jugador.get()
    Clave01 = Verificar_primera_clave.get()
    Clave02 = Verificar_segunda_clave.get()
    Contador_Errores = 0
    if Clave01 != Clave02:
        ClavesIncorrectas()
    else:
        Contador_Errores += (Validar_Usuario(Usuario01, Registro_Usuarios_Claves) + Validar_Clave(Clave01))
        if Contador_Errores == 0:
                archivo = open("usuarios.csv","a+")
                Texto_a_escribir = "\n" + Usuario01 + "," + Clave01
                archivo.write(Texto_a_escribir)
                archivo.close()
                Lista_Jugadores.append(Usuario01)
                if len(Lista_Jugadores) == MAXIMO_JUGADORES:
                    MaximoJugadoresAlcanzado()
                    Iniciar_Partida()
                else:
                    LoginCorrecto()

#Funcion que crea la interfaz gráfica.

def crear_ventana():
    """Esta función crea la ventana para registrar e ingresar los usuarios que jugaran al Pasapalabras.
    Autor: Steven Guerrero """
    #Definiendo variables globales para las funciones
    global Verificar_jugador
    global Verificar_primera_clave
    global Verificar_segunda_clave
    global ventana
    global Lista_Jugadores
    
    ventana = Tk()
    ventana.title("Ingreso y Registro de usuario")
    ventana.geometry("320x200")
    ventana.resizable(1,1)
    ventana.iconbitmap("Wizard_Hat.ico")
    ventana.config(bg="#385f7d")

    Verificar_jugador = StringVar()
    Verificar_primera_clave = StringVar()
    Verificar_segunda_clave = StringVar()
    archivo = open("usuarios.csv","r+")
    Registro_Usuarios_Claves = Crear_Diccionarios_Usuarios(archivo)
    archivo.close()
    Lista_Jugadores = []
    
    #Cuadro de Texto "Nombre Jugador"
    Usuario_Jugador= Label(ventana, text="Nombre Jugador:", bg="#385f7d",fg="white", font=("Century Gothic",9))
    #Usuario_Alumno.place(x=10, y=10)
    Usuario_Jugador.grid(row=0, column=0, padx="25", pady="10")
    
    #Cuadro de Entrada para Jugador
    Usuario_Jugador_Entry = Entry(ventana, textvariable=Verificar_jugador)
    Usuario_Jugador_Entry.grid(row=0, column=1, padx="10", pady="10") 
    
    #Cuadro de Texto "Clave"
    Primera_Clave = Label(ventana, text="Clave:", bg="#385f7d",fg="white", font=("Century Gothic",9))
    #Usuario_Alumno.place(x=10, y=10)
    Primera_Clave.grid(row=1, column=0, padx="25", pady="10", sticky="w")
    
    #Cuadro de Entrada para primera clave
    Primera_Clave_Entry = Entry(ventana, show="*", textvariable=Verificar_primera_clave)
    Primera_Clave_Entry.grid(row=1, column=1, padx="10", pady="10")
    
    #Cuadro de Texto "Repetir Clave"
    Segunda_Clave = Label(ventana, text="Repetir clave:", bg="#385f7d",fg="white", font=("Century Gothic",9))
    #Usuario_Alumno.place(x=10, y=10)
    Segunda_Clave.grid(row=2, column=0, padx="25", pady="10", sticky="w")
    
    #Cuadro de Entrada para primera clave
    Segunda_Clave_Entry = Entry(ventana, show="*", textvariable=Verificar_segunda_clave)
    Segunda_Clave_Entry.grid(row=2, column=1, padx="10", pady="10")
    
    #Boton Ingresar
    Ingresar = Button(ventana, text="Ingresar", command= lambda: Ingresar_usuario(Registro_Usuarios_Claves))
    Ingresar.place(x=117, y=150)
    
    #Boton Iniciar partida
    Iniciar = Button(ventana, text="Iniciar Partida", command=lambda: Iniciar_Partida())
    Iniciar.place(x=180, y=150)
    
    #Boton Registrar
    Registrar = Button(ventana, text="Registrar", command=lambda: Registrar_usuario(Registro_Usuarios_Claves))
    Registrar.place(x=50, y=150)
    
        
    ventana.mainloop()

#crear_ventana()

#import doctest
#print(doctest.testmod())