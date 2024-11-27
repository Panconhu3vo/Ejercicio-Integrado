import sys
import os
import tkinter as tk

# Función para manejar rutas dinámicas
def obtenerRutaRecurso(rutaRelativa):
    if hasattr(sys, '_MEIPASS'):
        # Ruta cuando está empaquetado con PyInstaller
        return os.path.join(sys._MEIPASS, rutaRelativa)
    else:
        # Ruta durante el desarrollo
        return os.path.abspath(rutaRelativa)

# Ruta al diccionario y al icono
rutaDiccionario = obtenerRutaRecurso("src/diccionario.py")
rutaIcono = obtenerRutaRecurso("ui/img/diccionarioimg.ico")

# Cargar el contenido de diccionario.py dinámicamente
diccionario = {}
try:
    with open(rutaDiccionario, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        exec(contenido, globals())  # Ejecuta el contenido de diccionario.py
except FileNotFoundError:
    print(f"No se pudo encontrar el archivo: {rutaDiccionario}")
    sys.exit(1)
except Exception as e:
    print(f"Error al cargar el diccionario: {e}")
    sys.exit(1)

# Función para limpiar bytes nulos en diccionario.py
def limpiarDiccionario():
    if not os.path.exists(rutaDiccionario):
        print(f"Error: El archivo {rutaDiccionario} no existe.")
        return

    with open(rutaDiccionario, "rb") as file:
        contenido = file.read()

    if b"\x00" in contenido:
        contenido = contenido.replace(b"\x00", b"")
        with open(rutaDiccionario, "wb") as file:
            file.write(contenido)

# Llama a la función para limpiar el diccionario
limpiarDiccionario()
from tkinter import messagebox

# ------------------------------------------------------
# Variables:
# ------------------------------------------------------

termino = tk.StringVar
nombreNT = tk.StringVar

# ------------------------------------------------------
# Funciones:
# ------------------------------------------------------

def verificarNombre(termino):
    termino = " ".join(termino.split())
    termino = termino.lower()
    for i in "abcdefghijklmnopqrstuvwxyz":
        if termino in list(diccionario[i].keys()):
            return True
            break
    return False 
 
 
# ------------------------------------------------------
# Funciones de Funcionalidades:
# ------------------------------------------------------
def FNlistarTerminos(event=None): 
    txtTerminosListados.configure(state="normal")

    for i in "zyxwvutsrqponmlkjihgfedcba":
        txtTerminosListados.insert("1.0", f"""{i}""" )
        for j in diccionario[i]:
            txtTerminosListados.configure(state="norma")
            txtTerminosListados.insert("1.0", f''' 
  Termino: {j}
  Definicion: {diccionario[i][j]["definicion"]}
  Traduccion: {diccionario[i][j]["traduccion"]}
  Categoria: {diccionario[i][j]["categoria"]}
''')
        txtTerminosListados.insert("1.0", f"\n{i.upper()}:\n")
    txtTerminosListados.configure(state="disable")

def FNFiltrar(event=None):
    letraBuscar = enIndiceFiltro.get().upper() 

    if letraBuscar in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":  
        patronBusqueda = f"{letraBuscar}:"
        idxInicio = "1.0"
        idxLetra = txtTerminosListados.search(patronBusqueda, idxInicio, stopindex="end")
        if idxLetra:
            txtTerminosListados.see(idxLetra)
            
def FNeliminarTermino(event=None):
    termino = enNombreET.get().strip()

    if verificarNombre(termino):
        confirmacion = messagebox.askyesno(
            "Confirmar Eliminación",
            f"¿Estás seguro de que deseas eliminar el término '{termino}'?"
        )
        if confirmacion:
            letraInicial = termino[0].lower()
            datos = diccionario[letraInicial].pop(termino, None)

            # Si no quedan términos en la letra, eliminar la letra del diccionario
            if not diccionario[letraInicial]:
                del diccionario[letraInicial]

            guardarDiccionario()
            limpiarDiccionario()

            # Actualizar consola con mensaje de éxito
            txtConsoleE.configure(state="normal")
            txtConsoleE.delete(1.0, tk.END)
            txtConsoleE.insert(
                "1.0",
                f"Término eliminado con éxito:\n"
                f"- Término: {termino}\n"
                f"- Definición: {datos['definicion']}\n"
                f"- Traducción: {datos['traduccion']}\n"
                f"- Categoría: {datos['categoria']}\n"
            )
            txtConsoleE.update_idletasks()  # Forzar actualización
            txtConsoleE.configure(state="disable")
        else:
            # Mensaje para cancelación
            txtConsoleE.configure(state="normal")
            txtConsoleE.delete(1.0, tk.END)
            txtConsoleE.insert("1.0", "Operación cancelada. No se eliminó ningún término.\n")
            txtConsoleE.update_idletasks()  # Forzar actualización
            txtConsoleE.configure(state="disable")
    else:
        # Mensaje si no se encuentra el término
        txtConsoleE.configure(state="normal")
        txtConsoleE.delete(1.0, tk.END)
        txtConsoleE.insert("1.0", f"El término '{termino}' no se encuentra en el diccionario.\n")
        txtConsoleE.update_idletasks()  # Forzar actualización
        txtConsoleE.configure(state="disable")

def FNagregarTermino(event=None):
    txtConsole.configure(state="normal")
    txtConsole.delete(1.0, tk.END)
    txtConsole.update_idletasks()
    
    # Obtener valores del formulario
    nombreTermino = enNombreNT.get().strip()
    definicionTermino = txtDefinicion.get(1.0, tk.END).strip()
    traduccionTermino = txtTraduccion.get(1.0, tk.END).strip()
    categoriaTermino = categoriaSelect.get()

    if verificarNombre(nombreTermino) == False:
        letraInicial = nombreTermino[0].lower()
        if letraInicial not in diccionario:
            diccionario[letraInicial] = {}
        diccionario[letraInicial][nombreTermino] = {
            "definicion": definicionTermino,
            "traduccion": traduccionTermino,
            "categoria": categoriaTermino,
        }
        guardarDiccionario()
        limpiarDiccionario()

        # Mensaje de éxito
        txtConsole.insert("1.0", "\n ¡¡¡Término agregado correctamente!!! \n")
    else:
        # Mensaje de término existente
        txtConsole.insert("1.0", "Término existente, ingresa uno nuevo.\n")
    
    txtConsole.configure(state="disable")

# Función para guardar el diccionario en el archivo
def guardarDiccionario():
    rutaArchivo = r"src\diccionario.py"
    with open(rutaArchivo, "w", encoding="utf-8") as archivo:
        # Escribir el encabezado del diccionario
        archivo.write("diccionario = {\n")
        
        # Obtener el total de letras
        totalLetras = len(diccionario)
        for j, (letra, terminos) in enumerate(diccionario.items(), start=1):
            archivo.write(f"    \"{letra}\": {{\n")
            
            # Escribir cada término dentro de la letra
            totalTerminos = len(terminos)
            for i, (termino, detalles) in enumerate(terminos.items(), start=1):
                archivo.write(f"        \"{termino}\": {{\n")
                archivo.write(f"            \"categoria\": {repr(detalles['categoria'])},\n")
                archivo.write(f"            \"definicion\": \"{detalles['definicion'].strip()}\",\n")
                archivo.write(f"            \"traduccion\": \"{detalles['traduccion'].strip()}\"\n")
                # Si no es el último término, agrega una coma
                if i < totalTerminos:
                    archivo.write("        },\n")
                else:
                    archivo.write("        }\n")  # Sin coma para el último término
            
            # Si no es la última letra, agrega una coma
            if j < totalLetras:
                archivo.write("    },\n")
            else:
                archivo.write("    }\n")  # Sin coma para la última letra
        
        archivo.write("}\n")

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
    
    # Limpiar Casillas Buscar Termino
    txtTerminoEncontrado.configure(state="normal")
    txtTerminoEncontrado.delete(1.0, tk.END)
    txtTerminoEncontrado.configure(state="disable")
    enBuscarTermino.delete(0, tk.END)
    
    # Limpiar Casillas Agregar Termino
    txtTraduccion.delete(1.0,tk.END)
    txtDefinicion.delete(1.0,tk.END)
    txtDefinicion.delete(1.0,tk.END)
    enNombreNT.delete(0,tk.END)
    
    txtConsole.configure(state="normal")
    txtConsole.delete(1.0, tk.END)
    txtConsole.configure(state="disable")
    categoriaSelect.set("Categoria")
    
    # Limpiar Casillas Eliminar Tërmino
    enNombreET.delete(0, tk.END)
    txtConsoleE.configure(state="normal")
    txtConsoleE.delete(1.0, tk.END)
    txtConsoleE.configure(state="disable")

    # Limpiar Casillas Listar Tërmino
    enIndiceFiltro.delete(0, tk.END)

# ------------------------------------------------------
# Funciones Interfaz:
# ------------------------------------------------------

def cerrarVentana():
    vn.destroy()

# ------------------------------------------------------
# Inicio:
# ------------------------------------------------------

def Inicio():
    nav.pack(fill="x")
    bordeInf.pack(fill="x", pady=(0, 5))
    instr.pack(side="top",pady=(10,15))
    bordeMenuPrincipal.pack(padx=110, pady=(0))
    menu.pack(side="left")
    footer.pack(fill="x")

def ocultarInicio():
    nav.pack_forget()
    bordeInf.pack_forget()
    instr.pack_forget()
    bordeMenuPrincipal.pack_forget()
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
vn.iconbitmap(rutaIcono)

# ------------------------------------------------------
# Barra de navegación Inicio
# ------------------------------------------------------

nav = tk.Frame(vn, bg="#1B1259", width=600, height=42)

tk.Label(
    nav, text="Diccionario Del Programador",
    font=("Roboto", 22, "bold"), fg="#F2F2F2", bg="#1B1259"
).pack(side="top")

# Borde inferior de la barra de navegación
bordeInf = tk.Frame(vn, height=2, bg="#d91f2b")

# ------------------------------------------------------
# Sección de Instrucciones
# ------------------------------------------------------

instr = tk.Frame(vn)

tk.Label(
    instr, text="Selecciona una opción:", 
    font=("Roboto", 16, "bold"), fg="#201161"
).pack(side="top", anchor="s")

# ------------------------------------------------------
# Menú principal
# ------------------------------------------------------

bordeMenuPrincipal = tk.Frame(vn, bg="#D92534", padx=4, pady=4)

menu = tk.Frame(bordeMenuPrincipal, width=380, height=240, bg="#1B1259")
menu.pack_propagate(False)

btnAgregarT = tk.Button(
    menu, text="Agregar Término", bg="#F2B705", fg="#F2F2F2",
    font=("Roboto", 12, "bold"), command=seccionAgregarTermino
)
btnAgregarT.pack(fill="both", expand=True, padx=110, pady=10)

btnEliminarT = tk.Button(
    menu, text="Eliminar Término", bg="#F2B705", fg="#F2F2F2", 
    font=("Roboto", 12, "bold"), command=seccionEliminarTermino
)
btnEliminarT.pack(fill="both", expand=True, padx=110, pady=11)

btnBuscarT = tk.Button(
    menu, text="Buscar Término", bg="#F2B705", fg="#F2F2F2", 
    font=("Roboto", 12, "bold"), command=seccionBuscarTermino
)
btnBuscarT.pack(fill="both", expand=True, padx=110, pady=11)

btnListarT = tk.Button(
    menu, text="Listar Términos", bg="#F2B705", fg="#F2F2F2", 
    font=("Roboto", 12, "bold"), command=seccionListarTermino
)
btnListarT.pack(fill="both", expand=True, padx=110, pady=11)

# ------------------------------------------------------
# Footer
# ------------------------------------------------------

footer = tk.Frame(vn)

btnAcercaDe = tk.Button(
    footer, text="Acerca de", bg="#d91f2b", fg="#F2F2F2", 
    font=("Roboto", 12, "bold"), command=seccionAcercaDe
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
    nav2, text="Diccionario del Programador", 
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
    menuIzquierdoAG, text="Nombre del Término: ",
    font=("Roboto",14,"bold"), fg="#F2F2F2",
    bg="#1B1259", justify="left", anchor="center"   
).pack(side="top", anchor="nw", padx=35, pady=(15,4))

enNombreNT = tk.Entry(menuIzquierdoAG)
enNombreNT.pack(side="top", anchor="nw", padx=39, pady=4)

txtConsole = tk.Text(menuIzquierdoAG, width=19, height=5, wrap="word")
txtConsole.pack(side="top", anchor="nw", expand=False, fill=None, padx=39, pady=4)
txtConsole.insert("1.0",""" 
Ingresa los datos para agregar un nuevo término 
                  
""")
txtConsole.configure(state="disable")

tk.Label(
    menuIzquierdoAG, text="Categoría: ",
    font=("Roboto",14,"bold"), fg="#F2F2F2",
    bg="#1B1259", justify="left", anchor="center"   
).pack(side="top", anchor="nw", padx=35, pady=(8))

# Menú desplegable de categorías en el Frame izquierdo
categoriasMenu = ['Estructuras de Datos', 'Funciones', 'Condicionales', 'Ciclos', 'General']
categoriaSelect = tk.StringVar()
categoriaSelect.set("Categoria")
menuCategoria = tk.OptionMenu(menuIzquierdoAG, categoriaSelect, *categoriasMenu)

menuCategoria.pack(side="top", anchor="nw", padx=(39,0), pady=(4))
btnAgregar= tk.Button(
    menuIzquierdoAG, text="Agregar",
    bg="#FFCE00", fg="#F2F2F2", 
    font=("Roboto", 10, "bold"),
    command=FNagregarTermino
)
btnAgregar.pack(side="right")

# Frame derecho (menuDerechoAG) configurado para el lado derecho
menuDerechoAG = tk.Frame(menuAgregarTermino, bg="#1b1259", width=255, height=338)
menuDerechoAG.pack_propagate(False)
menuDerechoAG.pack(side="right")

tk.Label(
    menuDerechoAG, text="Definición: ",
    font=("Roboto",14,"bold"),fg="#F2F2F2",
    bg="#1B1259",justify="left", anchor="center"   
).pack(side="top",anchor="nw",padx=35,pady=(15,4))

txtDefinicion = tk.Text(menuDerechoAG,width=25,height=5,wrap="word")
txtDefinicion.pack(side="top",anchor="nw",expand=False,fill=None,padx=39,pady=(4))

tk.Label(
    menuDerechoAG, text="Traducción: ",
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
    eliminarTermino, text="Eliminar Término",
    font=("Roboto",16,"bold"), fg="#1B1259"
).pack(side="top")

bordeEntradaDatos = tk.Frame(eliminarTermino, bg="#D92534", padx=4, pady=4)
bordeEntradaDatos.pack(side="left", padx=(37), pady=(16,26))

menuEliminarTermino = tk.Frame(bordeEntradaDatos,width=525, height=275, bg="#1B1259")
menuEliminarTermino.pack_propagate(False)
menuEliminarTermino.pack()

btnEliminar = tk.Button(
    menuEliminarTermino, text="Eliminar",
    bg="#FFCE00", fg="#F2F2F2", 
    font=("Roboto", 10, "bold"),
    command=FNeliminarTermino
)
btnEliminar.pack(side="right",anchor="ne",padx=(0, 39),pady=(15,4))

tk.Label(
    menuEliminarTermino, text="Nombre del Término: ",
    font=("Roboto",14,"bold"),fg="#F2F2F2",
    bg="#1B1259",justify="left", anchor="center"   
).pack(side="top",anchor="nw",padx=35,pady=(15,4))


enNombreET = tk.Entry(menuEliminarTermino)
enNombreET.bind("<Return>",FNeliminarTermino)
enNombreET.pack(side="top", anchor="nw", padx=39, pady=4)

txtConsoleE = tk.Text(menuEliminarTermino,width=75,height=10,wrap="word")
txtConsoleE.configure(state="disabled")
txtConsoleE.pack(side="top",anchor="nw",expand=True,fill=None,padx=(39,0),pady=(4))

# ------------------------------------------------------
# Sección "Bucar Término"
# ------------------------------------------------------

# Frame principal para "Buscar Término"
buscarTermino = tk.Frame(vn)

# Título de la sección
tk.Label(
    buscarTermino, text="Buscar Términos",
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
    listarTermino, text="Listar Términos",
    font=("Roboto",16,"bold"), fg="#1B1259"
).pack(side="top")

bordeListarTerminos = tk.Frame(listarTermino, bg="#D92534", padx=4, pady=4)
bordeListarTerminos.pack(side="left", padx=26, pady=(16,26))

menuListarTerminos = tk.Frame(bordeListarTerminos ,bg="#1b1259",width=525, height=385)
menuListarTerminos.pack(side="top",fill="x")

fmFiltroTerminos = tk.Frame(menuListarTerminos,bg="#1b1259")
fmFiltroTerminos.pack(side="top",fill="x")

tk.Label(
    fmFiltroTerminos,text="Filtra por letra: ",
    font=("Roboto",16,"bold"), fg="#f2f2f2",bg="#1b1259"
).pack(side="left",padx=(5,0),pady=(13,16))

enIndiceFiltro = tk.Entry(fmFiltroTerminos,width=2)
enIndiceFiltro.pack(side="left",padx=(90,12))
enIndiceFiltro.bind("<Return>",FNFiltrar)

btnFiltrar = tk.Button(
    fmFiltroTerminos,text="Filtrar",
    bg="#FFCE00", fg="#F2F2F2", 
    font=("Roboto", 10, "bold"),
    command=FNFiltrar    
)
btnFiltrar.pack(side="left",padx=(12),pady=7)

fmTeminosListados = tk.Frame(menuListarTerminos)
fmTeminosListados.pack()

txtTerminosListados = tk.Text(fmTeminosListados,width=65,height=25)
txtTerminosListados.configure(state="disable")
txtTerminosListados.pack(side="left",fill="both")
txtTerminosListados.bind("<Visibility>", FNlistarTerminos)

scrollbar = tk.Scrollbar(fmTeminosListados, orient="vertical", command=txtTerminosListados.yview)
scrollbar.pack(side="right", fill="y")
txtTerminosListados.config(yscrollcommand=scrollbar.set)
# ------------------------------------------------------
# Sección "Acerca De"
# ------------------------------------------------------

# Frame para la sección "Acerca de"
acercaDe = tk.Frame(vn)

# Título de la sección "Acerca de"
tk.Label(
    acercaDe, text="Diccionario del Programador, Inglés-Español",
    font=("Roboto", 12, "bold"), fg="#201161"
).pack(side="top", padx=(40), pady=10)

bordeAcercaDe = tk.Frame(acercaDe, bg="#D92534", padx=4, pady=4)
bordeAcercaDe.pack(side="left", padx=(26,13), pady=(16,26))

# Texto explicativo sobre el proyecto, en un campo de solo lectura
txtAcecaDeP1 = tk.Text(
    bordeAcercaDe, wrap="word", height=39,
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
txtAcecaDeP1.pack(side="top")

# ------------------------------------------------------
# Ejecutar la aplicación
# ------------------------------------------------------

Inicio()
vn.mainloop()