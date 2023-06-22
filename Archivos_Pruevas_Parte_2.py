from tkinter import messagebox

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

# -------- Aquí empiezan las pruebas unitarias --------

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


#-------- Funcion para iniciar pruebas doctest --------

import doctest
print(doctest.testmod())