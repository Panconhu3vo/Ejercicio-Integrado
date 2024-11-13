import tkinter as tk 
import sys
import os

ruta_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.insert(0, ruta_src)

from model import *
from diccionario import diccionario
# ------------------------------------------------------
# Variables:
# ------------------------------------------------------

termino = tk.StringVar

# ------------------------------------------------------
# Funciones:
# ------------------------------------------------------

# ------------------------------------------------------
# Funciones de Funcionalidades:
# ------------------------------------------------------

# Funcion buscar termino
def FNbuscarTermino(event=None):
    
    termino = enBuscarTermino.get()
    if verificarNombre(termino) == True:
        txtTerminoEncontrado.configure(state="normal")
        txtTerminoEncontrado.insert("1.0",
        f'''Termino: {termino}
  Definicion: {diccionario[termino[0]][termino]["definicion"]}
  Traduccion: {diccionario[termino[0]][termino]["traduccion"]}
  Categoria: {diccionario[termino[0]][termino]["categoria"]}
        
        ''')
        txtTerminoEncontrado.configure(state="disable")
    else:
        txtTerminoEncontrado.configure(state="normal")
        txtTerminoEncontrado.insert("1.0","""
      ¡¡¡Termino no encontrado!!!
     (Asegurate de escribirlo bien)
                                    """)
        txtTerminoEncontrado.configure(state="disable")
         
# Funcion limpiar casillas
def limpiarCasillas():
    txtTerminoEncontrado.configure(state="normal")
    txtTerminoEncontrado.delete(1.0, tk.END)
    txtTerminoEncontrado.configure(state="disable")
    enBuscarTermino.delete(0, tk.END)
    
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
    vn.geometry("600x530")
    listarTermino.pack(fill="both")

def ocultarSeccionListarTermino():
    ocultarNavegadorEntreSecciones()
    listarTermino.pack_forget()

# ------------------------------------------------------
# Seccion Acerca De:
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
    limpiarCasillas()
    ocultarSeccionAgregarTermino()
    ocultarSeccionEliminarTermino()
    ocultarSeccionBuscarTermino()
    ocultarSeccionListarTermino()
    ocultarSeccionAcercaDe()
    Inicio()

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

menu = tk.Frame(vn, width=270, height=270, bg="#1B1259")

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
    nav2, text="Volver", bg="#d91f2b", fg="#F2F2F2", 
    font=("Roboto", 12, "bold"), command=volver
)
btnVolver.pack(side="right", padx=(0, 10), pady=2)

# ------------------------------------------------------
# Sección "Agregar Término"
# ------------------------------------------------------

# Frame principal para "Agregar Término"
agregarTermino = tk.Frame(vn)

# Título de la sección "Agregar Término"
tk.Label(
    agregarTermino, text="Agregar Término",
    font=("Roboto", 16, "bold"), fg="#1B1259"
).pack(side="top")

# Borde de entrada de datos
bordeEntradaDatos = tk.Frame(agregarTermino, bg="#D92534", padx=4, pady=4)
bordeEntradaDatos.pack(side="left", padx=38, pady=(16,26))

# Frame contenedor para menú izquierdo y derecho
menuAgregarTermino = tk.Frame(bordeEntradaDatos, bg="#1b1259", width=525, height=340)
menuAgregarTermino.pack_propagate(False)
menuAgregarTermino.pack(side="left")

# Frame izquierdo (menuIzquierdoAG) configurado para el lado izquierdo
menuIzquierdoAG = tk.Frame(menuAgregarTermino, bg="#1b1259", width=260, height=338)
menuIzquierdoAG.pack(side="left", anchor="nw")

tk.Label(
    menuIzquierdoAG, text="Nombre Termino: ",
    font=("Roboto",14,"bold"), fg="#F2F2F2",
    bg="#1B1259", justify="left", anchor="center"   
).pack(side="top", anchor="nw", padx=35, pady=(15,4))

enNombreNT = tk.Entry(menuIzquierdoAG)
enNombreNT.pack(side="top", anchor="nw", padx=39, pady=4)

txtConsole = tk.Text(menuIzquierdoAG, width=19, height=5, wrap="word")
txtConsole.pack(side="top", anchor="nw", expand=False, fill=None, padx=39, pady=4)

tk.Label(
    menuIzquierdoAG, text="Categoria: ",
    font=("Roboto",14,"bold"), fg="#F2F2F2",
    bg="#1B1259", justify="left", anchor="center"   
).pack(side="top", anchor="nw", padx=35, pady=(8))

# Menú desplegable de categorías en el Frame izquierdo
categoriasMenu = ('Estructuras de Datos', 'Funciones', 'Condicionales', 'Ciclos', 'General')
categoriaSelect = tk.StringVar()
categoriaSelect.set("Categoria")
menuCategoria = tk.OptionMenu(menuIzquierdoAG, categoriaSelect, *categoriasMenu)
menuCategoria.pack(side="top", anchor="nw", padx=39, pady=(4))

# Frame derecho (menuDerechoAG) configurado para el lado derecho
menuDerechoAG = tk.Frame(menuAgregarTermino, bg="#1b1259", width=255, height=338)
menuDerechoAG.pack_propagate(False)
menuDerechoAG.pack(side="right")

tk.Label(
    menuDerechoAG, text="Definicion: ",
    font=("Roboto",14,"bold"),fg="#F2F2F2",
    bg="#1B1259",justify="left", anchor="center"   
).pack(side="top",anchor="nw",padx=35,pady=(15,4))

txtDefinicion = tk.Text(menuDerechoAG,width=25,height=5,wrap="word")
txtDefinicion.pack(side="top",anchor="nw",expand=False,fill=None,padx=39,pady=(4))

tk.Label(
    menuDerechoAG, text="Traduccion: ",
    font=("Roboto",14,"bold"),fg="#F2F2F2",
    bg="#1B1259",justify="left", anchor="center"   
).pack(side="top",anchor="nw",padx=35,pady=(4))

txtTraduccion = tk.Text(menuDerechoAG,width=25,height=5,wrap="word")
txtTraduccion.pack(side="top",anchor="nw",expand=False,fill=None,padx=39,pady=(4))



# ------------------------------------------------------
# Sección "Eliminar Término"
# ------------------------------------------------------

eliminarTermino = tk.Frame(vn)

tk.Label(
    eliminarTermino, text="Eliminar Termino",
    font=("Roboto",16,"bold"), fg="#1B1259"
).pack(side="top")

entradaDatos = tk.Frame(eliminarTermino, width=270, height=270, bg="#1B1259")
entradaDatos.pack_propagate(False)
entradaDatos.pack(side="top", padx=35, pady=25)

tk.Label(
    entradaDatos, text='''Ingresa el nombre del término: ''', font=("Roboto", 10, "bold"),
    fg="white", bg="#1B1259", justify="center", anchor="center"   
).pack(side="top", pady=15)

enEliminarTermino = tk.Entry(entradaDatos)
enEliminarTermino.bind("<Return>", FNbuscarTermino)
enEliminarTermino.pack(side="top", padx=10, pady=10)

lbTerminoEliminado = tk.Label(
    entradaDatos, font=("Roboto", 10, "bold"),
    fg="white", bg="#1B1259", justify="center", anchor="center"   
)
lbTerminoEliminado.pack(side="top", pady=(10,5))

# ------------------------------------------------------
# Sección "Bucar Término"
# ------------------------------------------------------

# Frame principal para "Buscar Término"
buscarTermino = tk.Frame(vn)

# Título de la sección
tk.Label(
    buscarTermino, text="Buscar Termino",
    font=("Roboto",16,"bold"), fg="#1B1259"
).pack(side="top")

bordeEntradaDatos = tk.Frame(buscarTermino, bg="#D92534", padx=4, pady=4)
bordeEntradaDatos.pack(side="left", padx=(26,13), pady=(16,26))

# Frame para entrada de datos dentro del borde
entradaDatos = tk.Frame(bordeEntradaDatos, width=160, height=270, bg="#1B1259", relief="solid")
entradaDatos.pack_propagate(False)
entradaDatos.pack()


# Instrucción para ingresar término
tk.Label(
    entradaDatos, text='''Ingresa el
término: ''', font=("Roboto", 14, "bold"),
    fg="white", bg="#1B1259", justify="left", anchor="center"   
).pack(side="top", pady=(10,5),padx=(14),anchor="nw")

# Campo de entrada, presionar Enter para buscar
enBuscarTermino = tk.Entry(entradaDatos)
enBuscarTermino.bind("<Return>", FNbuscarTermino)
enBuscarTermino.pack(side="top", padx=14, pady=10)

# Botón Buscar
btnBuscar = tk.Button(
    entradaDatos, text="Buscar",
    bg="#FFCE00", fg="#F2F2F2", 
    font=("Roboto", 10, "bold"),
    command=FNbuscarTermino
)
btnBuscar.pack(side="left", pady=15,padx=(14,7))

# Botón Limpiar
btnLimpiar = tk.Button(
    entradaDatos, text="Limpiar",
    bg="#FFCE00", fg="#F2F2F2", 
    font=("Roboto", 10, "bold"),
    command=limpiarCasillas
)
btnLimpiar.pack(side="right", pady=20,padx=(7, 14))

bordeMuestraDatos = tk.Frame(buscarTermino, bg="#D92534", padx=4, pady=4)
bordeMuestraDatos.pack(side="left", padx=(13,26), pady=(16,26))

# Frame para mostrar resultados
muestraDeDatos = tk.Frame(bordeMuestraDatos, width=350, height=270, bg="#1B1259")
muestraDeDatos.pack_propagate(False)
muestraDeDatos.pack(side="left")

# Área de texto de solo lectura para el resultado
txtTerminoEncontrado = tk.Text(muestraDeDatos, wrap="word", width=300, height=200, state="disable")
txtTerminoEncontrado.pack(side="top", padx=10, pady=10)


# ------------------------------------------------------
# Sección "Listar Término"
# ------------------------------------------------------

listarTermino = tk.Frame(vn)

tk.Label(
    listarTermino, text="Listar Termino",
    font=("Roboto",16,"bold"), fg="#1B1259"
).pack(side="top")

terminosListados = tk.Frame(listarTermino,width=550,height=350,bg="#d91f2b")
terminosListados.pack_propagate(False)
terminosListados.pack(side="top",padx=25)

mostrarTerminos = tk.Text(
    terminosListados,width=550,
    height=350,state="disable",wrap="word"
)

mostrarTerminos.pack(side="top",padx=5,pady=5)

menuFiltrar = tk.Frame(listarTermino,width=550,height=70,bg="#1b1259")
menuFiltrar.propagate(False)
menuFiltrar.pack(side="top",padx=25)

tk.Label(
    menuFiltrar, text="Ingresa al letra para filtrar: ",
    font=("Roboto",12,"bold"), fg="#f2f2f2",bg="#1b1259"
).pack(side="top")

filtro = tk.Frame(menuFiltrar, bg="#1b1259")
filtro.pack(side="top")

enLetra = tk.Entry(filtro,width=3)
enLetra.pack(side="left",padx=10)

btnFiltrar = tk.Button(
    filtro, text="Filtrar",
    bg="#FFCE00", fg="#F2F2F2", 
    font=("Roboto", 10, "bold")
)
btnFiltrar.pack(side="left",padx=10)
# ------------------------------------------------------
# Sección "Acerca De"
# ------------------------------------------------------

# Frame para la sección "Acerca de"
acercaDe= tk.Frame(vn)

# Título de la sección "Acerca de"
lbTitulo = tk.Label(
    acercaDe, text="Diccionario del Programador, Inglés-Español",
    font=("Roboto", 12, "bold"), fg="#201161"
)
lbTitulo.pack(side="top", padx=(40), pady=10)

# Texto explicativo sobre el proyecto, en un campo de solo lectura
txtAcecaDeP1 = tk.Text(
    acercaDe, wrap="word", height=39,
    font=("Roboto", 11)
)

# Insertar información sobre el proyecto y colaboradores
txtAcecaDeP1.insert(
    "1.0", f"""Este proyecto, se desarrolla como un ejercicio integrado de colaboración entre estudiantes de programación. Su objetivo es crear una herramienta práctica para traducir términos técnicos del inglés al español, ayudando a futuros programadores a comprender y utilizar el vocabulario técnico en su aprendizaje y desarrollo profesional.

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

# Configuración de solo lectura y ubicación para el texto de información
txtAcecaDeP1.configure(state="disabled")
txtAcecaDeP1.pack(side="top", padx=(40), pady=10)

# ------------------------------------------------------
# Ejecutar la aplicación
# ------------------------------------------------------
Inicio()
vn.mainloop()