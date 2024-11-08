
import tkinter as tk 
# import sys
# import os

# ruta_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
# sys.path.insert(0, ruta_src)

# from diccionarioDelProgramador import *
# from diccionario import *

# ------------------------------------------------------
# Funciones:
# ------------------------------------------------------

# ------------------------------------------------------
# Funciones Interfaz:
# ------------------------------------------------------


def cerrarVentana():
    """Cierra la ventana principal."""
    vn.destroy()

# ------------------------------------------------------
# Inicio:
# ------------------------------------------------------

def Inicio():
    nav.pack(fill="x")
    bordeInf.pack(fill="x", pady=(0, 5))
    instr.pack(fill="x")
    menu.pack(side="top")
    footer.pack(fill="x", pady=(15, 0))

def ocultarInicio():
    nav.pack_forget()
    bordeInf.pack_forget()
    instr.pack_forget()
    menu.pack_forget()
    footer.pack_forget()
# ------------------------------------------------------
# Navegador Secciones:
# ------------------------------------------------------

def navegadorEntreSecciones():
    nav2.pack(fill="x")
    bordeInf.pack(fill="x", pady=(0, 5))

def ocultarNavegadorEntreSecciones():
    nav2.pack_forget()
    bordeInf.pack_forget()
# ------------------------------------------------------
# Agregar Termino:
# ------------------------------------------------------

def seccionAgregarTermino():
    ocultarInicio()
    navegadorEntreSecciones()
    agregarTermino.pack(fill="both")

def ocultarSeccionAgregarTermino():
    ocultarNavegadorEntreSecciones()
    agregarTermino.pack_forget()

# ------------------------------------------------------
# Eliminar Termino:
# ------------------------------------------------------

def seccionEliminarTermino():
    ocultarInicio()
    navegadorEntreSecciones()
    eliminarTermino.pack(fill="both")

def ocultarSeccionEliminarTermino():
    ocultarNavegadorEntreSecciones()
    eliminarTermino.pack_forget()

# ------------------------------------------------------
# Buscar Termino:
# ------------------------------------------------------

def seccionBuscarTermino():
    ocultarInicio()
    navegadorEntreSecciones()
    buscarTermino.pack(fill="both")

def ocultarSeccionBuscarTermino():
    ocultarNavegadorEntreSecciones()
    buscarTermino.pack_forget()

# ------------------------------------------------------
# listar Termino:
# ------------------------------------------------------

def seccionListarTermino():
    ocultarInicio()
    navegadorEntreSecciones()
    listarTermino.pack(fill="both")

def ocultarSeccionListarTermino():
    ocultarNavegadorEntreSecciones()
    listarTermino.pack_forget()

# ------------------------------------------------------
# listar Termino:
# ------------------------------------------------------

def seccionAcercaDe():
    ocultarInicio()
    navegadorEntreSecciones()
    vn.geometry("600x530")
    acercaDe.pack(fill="both")

def ocultarSeccionAcercaDe():
    ocultarNavegadorEntreSecciones()
    acercaDe.pack_forget()


# ------------------------------------------------------
# Volver:
# ------------------------------------------------------

def volver():
    vn.geometry("600x420")
    """Vuelve al menú principal ocultando otras secciones."""
    ocultarSeccionAgregarTermino()
    ocultarSeccionEliminarTermino()
    ocultarSeccionBuscarTermino()
    ocultarSeccionListarTermino()
    ocultarSeccionAcercaDe()
    Inicio()

# ------------------------------------------------------
# Funciones Funcionalidades:
# ------------------------------------------------------


# ------------------------------------------------------
# Configuración de la ventana principal
# ------------------------------------------------------

vn = tk.Tk()
vn.configure(bg="#F2F2F2")
vn.geometry("600x420")
vn.resizable(False, False)
vn.title("Diccionario del Programador")
vn.iconbitmap("ui\img\diccionarioimg.ico")


# ------------------------------------------------------
# Barra de navegación Inicio
# ------------------------------------------------------

nav = tk.Frame(vn, bg="#1B1259", width=600, height=42)

lbnav = tk.Label(
    nav, text="Diccionario Del Programador",
    font=("Roboto", 22, "bold"), fg="#F2F2F2", bg="#1B1259"
)
lbnav.pack(side="top")

# Borde inferior de la barra de navegación
bordeInf = tk.Frame(vn, height=2, bg="#d91f2b")

# ------------------------------------------------------
# Sección de Instrucciones
# ------------------------------------------------------

instr = tk.Frame(vn, height=67)

lbInstr = tk.Label(
    instr, text="Ingresa una Opción:", 
    font=("Roboto", 16, "bold"), fg="#201161"
)
lbInstr.pack(side="top", anchor="s", pady=15)


# ------------------------------------------------------
# Menú principal
# ------------------------------------------------------

menu = tk.Frame(vn, width=270, height=220, bg="#1B1259")

btnAgregarT = tk.Button(
    menu, text="Agregar Término", bg="#F2B705", fg="#F2F2F2",
    font=("Roboto", 12, "bold"), command=seccionAgregarTermino
)
btnAgregarT.pack(fill="both", expand=True, padx=60, pady=10)

btnEliminarT = tk.Button(
    menu, text="Eliminar Término", bg="#F2B705", fg="#F2F2F2", 
    font=("Roboto", 12, "bold"),command=seccionEliminarTermino
)
btnEliminarT.pack(fill="both", expand=True, padx=60, pady=11)

btnBuscarT = tk.Button(
    menu, text="Buscar Término", bg="#F2B705", fg="#F2F2F2", 
    font=("Roboto", 12, "bold"),command=seccionBuscarTermino
)
btnBuscarT.pack(fill="both", expand=True, padx=60, pady=11)

btnListarT = tk.Button(
    menu, text="Listar Término", bg="#F2B705", fg="#F2F2F2", 
    font=("Roboto", 12, "bold"),command=seccionListarTermino
)
btnListarT.pack(fill="both", expand=True, padx=60, pady=11)

# ------------------------------------------------------
# Footer
# ------------------------------------------------------

footer = tk.Frame(vn)

btnAcercaDe = tk.Button(
    footer, text="Acerca De", bg="#d91f2b", fg="#F2F2F2", 
    font=("Roboto", 12, "bold"),command=seccionAcercaDe
)
btnAcercaDe.pack(pady=10, padx=15, side="right")

btnSalir = tk.Button(
    footer, text="Salir", bg="#d91f2b", fg="#F2F2F2", 
    font=("Roboto", 12, "bold"), command=cerrarVentana
)
btnSalir.pack(pady=10, padx=15, side="left")

# ------------------------------------------------------
# Barra de navegación secundaria  (para secciones internas)
# ------------------------------------------------------

nav2 = tk.Frame(vn, bg="#1B1259", width=600, height=42)

lbnav2 = tk.Label(
    nav2, text="Diccionario Del Programador", 
    font=("Roboto", 22, "bold"), fg="#F2F2F2", bg="#1B1259"
)
lbnav2.pack(side="left", padx=(40, 0))

btnVolver = tk.Button(
    nav2, text="Volver", bg="#FFCE00", fg="#F2F2F2", 
    font=("Roboto", 12, "bold"), command=volver
)
btnVolver.pack(side="right", padx=(0, 10), pady=2)

# ------------------------------------------------------
# Sección "Agregar Término"
# ------------------------------------------------------

agregarTermino = tk.Frame(vn)

tk.Label(
    agregarTermino, text="Agregar Término",
    font=("Roboto", 16, "bold"), fg="#1B1259"
).pack(side="top", pady=10)


fmAgregarTermino = tk.Frame(agregarTermino, width=500, height=270, bg="#1B1259")
fmAgregarTermino.pack_propagate(False)
fmAgregarTermino.pack(side="top", padx=25, pady=15)

fmNNuevoTermino = tk.Frame(fmAgregarTermino,width=490,height=66,bg="#1b1259")
fmNNuevoTermino.pack_propagate(False)
fmNNuevoTermino.pack(side="top")
             
tk.Label(
    fmNNuevoTermino, text="Nuevo término: ",
    font=("Roboto", 10, "bold"), fg="#F2F2F2", bg="#1B1259", anchor="w"
).pack(side="top", padx=10, pady=(10, 2), anchor="w")  

nombreNuevoTermino = tk.Entry(fmNNuevoTermino)
nombreNuevoTermino.pack(side="left", anchor="n", padx=12, pady=(0, 10))  

fmDNuevoTermino = tk.Frame(fmAgregarTermino,width=490,height=66,bg="#1b1259")
fmDNuevoTermino.pack_propagate(False)
fmDNuevoTermino.pack(side="top")

tk.Label(
    fmDNuevoTermino, text="Definición: ",
    font=("Roboto", 10, "bold"), fg="#F2F2F2", bg="#1B1259", anchor="w"
).pack(side="top", padx=10, pady=(10, 2), anchor="w")

definicionNuevoTermino = tk.Text(fmDNuevoTermino, width=50,height=30)  
definicionNuevoTermino.pack(side="left", anchor="n", padx=12, pady=(0, 5))

fmTNuevoTermino = tk.Frame(fmAgregarTermino,width=490,height=66,bg="#1b1259")
fmTNuevoTermino.pack_propagate(False)
fmTNuevoTermino.pack(side="top")
 
tk.Label(
    fmTNuevoTermino, text="Traduccion: ",
    font=("Roboto", 10, "bold"), fg="#F2F2F2", bg="#1B1259", anchor="w"
).pack(side="top", padx=10, pady=(10, 2), anchor="w")

taduccionNuevoTermino = tk.Text(fmTNuevoTermino, width=50,height=30)  
taduccionNuevoTermino.pack(side="left", anchor="n", padx=12, pady=(0, 5))

fmCNuevoTermino = tk.Frame(fmAgregarTermino,width=490,height=66,bg="#1b1259")
fmCNuevoTermino.pack_propagate(False)
fmCNuevoTermino.pack(side="top")

tk.Label(
    fmCNuevoTermino, text="Categoria: ",
    font=("Roboto", 10, "bold"), fg="#F2F2F2", bg="#1B1259", anchor="w"
).pack(side="top", padx=10, pady=(10, 2), anchor="w")

taduccionNuevoTermino = tk.Text(fmCNuevoTermino, width=50,height=30)  
taduccionNuevoTermino.pack(side="left", anchor="n", padx=12, pady=(0, 5))

# ------------------------------------------------------
# Sección "Eliminar Término"
# ------------------------------------------------------

eliminarTermino = tk.Frame(vn)

# ------------------------------------------------------
# Sección "Bucar Término"
# ------------------------------------------------------

buscarTermino = tk.Frame(vn)

tk.Label(
    buscarTermino, text="Buscar Termino",
    font=("Roboto",16,"bold"),fg="#1B1259"
).pack(side="top")

entradaDatos = tk.Frame(buscarTermino,width=160,height=270)
entradaDatos.configure(bg="#1B1259")
entradaDatos.pack_propagate(False)
entradaDatos.pack(side="left", padx=(30),pady=25)

tk.Label(
    entradaDatos, text='''Ingresa el nombre 
    del término: ''',font=("Roboto", 10, "bold"), 
    fg="white", bg="#1B1259",
    justify="center",anchor="center"   
).pack(side="top", pady=5)

enBuscarTermino = tk.Entry(entradaDatos)
enBuscarTermino.pack(side="top",padx=10,pady=10)

btnBuscar = tk.Button(
    entradaDatos, text="Buscar",
    bg="#FFCE00", fg="#F2F2F2", 
    font=("Roboto", 12, "bold")
)
btnBuscar.pack(side="top",pady=15)

muestraDeDatos = tk.Frame(buscarTermino,width=350,height=270)
muestraDeDatos.configure(bg="#1B1259")
muestraDeDatos.pack_propagate(False)
muestraDeDatos.pack(side="left", padx=(30),pady=25)

txtTerminoEncontrado = tk.Text(muestraDeDatos, wrap="word",width=300,height=200)
txtTerminoEncontrado.configure(state="disable")
txtTerminoEncontrado.pack(side="top",padx=10,pady=10)

# ------------------------------------------------------
# Sección "Listar Término"
# ------------------------------------------------------

listarTermino = tk.Frame(vn)

# ------------------------------------------------------
# Sección "Acerca De"
# ------------------------------------------------------

acercaDe= tk.Frame(vn)

lbTitulo = tk.Label(
    acercaDe, text="Diccionario del Programador, Inglés-Español",
    font=("Roboto", 12, "bold"),fg="#201161"
)

lbTitulo.pack(side="top", padx=(40),pady=10)

txtAcecaDeP1 = tk.Text(
    acercaDe, wrap="word", height=39,
    font=("Roboto",11)
)

txtAcecaDeP1.insert(
    "1.0","""Este proyecto, se desarrolla como un ejercicio integrado de colaboración entre estudiantes de programación. Su objetivo es crear una herramienta práctica para traducir términos técnicos del inglés al español, ayudando a futuros programadores a comprender y utilizar el vocabulario técnico en su aprendizaje y desarrollo profesional.

Colaboradores

El equipo está conformado por estudiantes comprometidos con la creación y perfeccionamiento de esta herramienta. A continuación se enlistan los miembros y sus respectivos nombres de usuario en GitHub:

Juan Yañez - @Panconhu3vo
Thiare Carvacho - @thiareecart
Jose Cheuquefilo - @josecheuquefilo
Juan Alchao - @Juan777ac
Feguens Louissaint - @kanabuggi
Millaray Perez - Usuario pendiente

Tecnologías Utilizadas

Para la creación del diccionario, empleamos la librería Tkinter, que permite una interfaz gráfica interactiva, y la herramienta DOT para generar diagramas de flujo, facilitando la visualización de los procesos dentro de la aplicación."""
)

txtAcecaDeP1.configure(state="disabled")
txtAcecaDeP1.pack(side="top", padx=(40),pady=10)



# ------------------------------------------------------
# Ejecutar la aplicación
# ------------------------------------------------------
Inicio()
vn.mainloop()
