from tkinter import *
from tkinter import messagebox
from Etapa_04_y_main import *

#Constantes
USUARIO = 0
CLAVE = 1
USUARIO_CORTE = "0000000000"
CLAVE_CORTE = "000000"
CONDICION_CORTE_REGISTRO = USUARIO_CORTE + "," + CLAVE_CORTE
MAXIMO_JUGADORES = 4

def LoginIncorrecto():
    messagebox.showerror("Error de inicio de sesión", "El usuario o clave estan incorrectos")

def ClavesIncorrectas():
    messagebox.showerror("Error de inicio de sesión", "Las contraseñas introducidas no coinciden")
    
def LoginCorrecto():
    messagebox.showinfo("Login correcto", "Usuario y Clave correctos.\n Jugador agregado a la partida")
    
def UsuarioExistente():
    messagebox.showerror("Error de inicio de sesión", "Este usuario ya existe")

def UsuarioAgregado():
    messagebox.showerror("Error de inicio de sesión", "Este usuario ya forma parte de esta partida")

def MaximoJugadoresAlcanzado():
    messagebox.showinfo("Login correcto", "Usuario y Clave correctos\n Jugador agregado a la partida\n Máximo de Jugadores alcanzado, se iniciará partida")
    
def Iniciar_Partida():
    archivo.close()
    ventana.destroy()
    main()

def Leer_Lineas_de_Usuarios(archivo):
    linea = archivo.readline()
    if (not(linea)):
        linea = CONDICION_CORTE_REGISTRO
    linea = linea.rstrip()
    return linea.split(',')

def Crear_Diccionarios_Usuarios(archivo):
    Registro_Usuarios_Claves = {}
    Usuario_Clave =["",""]
    while (Usuario_Clave[USUARIO] != USUARIO_CORTE and Usuario_Clave[CLAVE] != CLAVE_CORTE):
        Usuario_Clave = Leer_Lineas_de_Usuarios(archivo)
        Registro_Usuarios_Claves[Usuario_Clave[USUARIO]] = Usuario_Clave[CLAVE]
    return Registro_Usuarios_Claves

#Falta verificar que se haya alcanzado el máximo de jugadores.
#Faltan condiciones de verificacion de cusuario y claves validos

def obtener_usuarios_claves(): 
    Registro_Usuarios_Claves = Crear_Diccionarios_Usuarios(archivo)
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
            if len(Lista_Jugadores) == MAXIMO_JUGADORES:
                MaximoJugadoresAlcanzado()
                Iniciar_Partida()
            else:
                LoginCorrecto()
        else:
            LoginIncorrecto()
        
def Registrar_usuario():
    #Verificar que usuario existe, sino agregarlo al archivo csv.
    Registro_Usuarios_Claves = Crear_Diccionarios_Usuarios(archivo)
    Usuario01 = Verificar_jugador.get()
    Clave01 = Verificar_primera_clave.get()
    Clave02 = Verificar_segunda_clave.get()
    if Clave01 != Clave02:
        ClavesIncorrectas()
    else:
        if Usuario01 in Registro_Usuarios_Claves.keys():
            UsuarioExistente()
        else:
            #Hay que agregar el usuario y su clave al archivo csv y el nombre del jugador a la lista de jugadores
            LoginIncorrecto()

def crear_ventana():
    #Definiendo variables globales para las funciones
    global Verificar_jugador
    global Verificar_primera_clave
    global Verificar_segunda_clave
    global archivo
    global ventana
    global Lista_Jugadores
    
    ventana = Tk()
    ventana.title("Ingreso y Registro de usuario")
    ventana.geometry("300x130")
    ventana.resizable(0,0)
    ventana.iconbitmap("Wizard_Hat.ico")
    ventana.config(bg="#385f7d")

    Verificar_jugador = StringVar()
    Verificar_primera_clave = StringVar()
    Verificar_segunda_clave = StringVar()
    archivo = open("usuarios.csv","a+")
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
    Ingresar = Button(ventana, text="Ingresar", command=obtener_usuarios_claves)
    Ingresar.place(x=130, y=90)
    
    #Boton Iniciar partida
    Iniciar = Button(ventana, text="Iniciar Partida", command=Iniciar_Partida)
    Iniciar.place(x=200, y=90)
    
    #Boton Registrar
    Registrar = Button(ventana, text="Registrar", command=Registrar_usuario)
    Registrar.place(x=50, y=90)
    
        
    ventana.mainloop()




crear_ventana()