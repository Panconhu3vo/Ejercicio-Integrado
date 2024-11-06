import tkinter as tk 

# ------------------------------------------------------
# Funciones:
# ------------------------------------------------------

def cerrarVentana():
    """Cierra la ventana principal."""
    vn.destroy()

def volver():
    """Vuelve al menú principal ocultando otras secciones."""
    nav.pack(fill="x")
    instr.pack(fill="x")
    menu.pack(side="top")
    footer.pack(fill="x")
    nav2.pack_forget()
    agregarTermino.pack_forget()

def seccionAT():
    """Muestra la sección para agregar término y oculta el menú principal."""
    agregarTermino.pack(fill="both")
    nav2.pack(fill="x")
    nav.pack_forget()
    instr.pack_forget()
    menu.pack_forget()
    footer.pack_forget()


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
# Barra de navegación principal
# ------------------------------------------------------

nav = tk.Frame(vn, bg="#1B1259", width=600, height=42)
nav.pack(fill="x")

lbnav = tk.Label(
    nav, text="Diccionario Del Programador",
    font=("Roboto", 22, "bold"), fg="#F2F2F2", bg="#1B1259"
)
lbnav.pack(side="top")

# Borde inferior de la barra de navegación
bordeInf = tk.Frame(vn, height=2, bg="#d91f2b")
bordeInf.pack(fill="x", pady=(0, 5))


# ------------------------------------------------------
# Barra de navegación secundaria (para secciones internas)
# ------------------------------------------------------

nav2 = tk.Frame(vn, bg="#D92534", width=600, height=42)

lbnav2 = tk.Label(
    nav2, text="Diccionario Del Programador", 
    font=("Roboto", 22, "bold"), fg="#F2F2F2", bg="#D92534"
)
lbnav2.pack(side="left", padx=(40, 0))

btnVolver = tk.Button(
    nav2, text="Volver", bg="#FFCE00", fg="#F2F2F2", 
    font=("Roboto", 12, "bold"), command=volver
)
btnVolver.pack(side="right", padx=(0, 10), pady=5)


# ------------------------------------------------------
# Sección de Instrucciones
# ------------------------------------------------------

instr = tk.Frame(vn, height=67)
instr.pack(fill="x")

lbInstr = tk.Label(
    instr, text="Ingresa una Opción:", 
    font=("Roboto", 16, "bold"), fg="#201161"
)
lbInstr.pack(side="top", anchor="s", pady=15)


# ------------------------------------------------------
# Menú principal
# ------------------------------------------------------

menu = tk.Frame(vn, width=270, height=220, bg="#1B1259")
menu.pack(side="top")

btnAgregarT = tk.Button(
    menu, text="Agregar Término", bg="#F2B705", fg="#F2F2F2",
    font=("Roboto", 12, "bold"), command=seccionAT
)
btnAgregarT.pack(fill="both", expand=True, padx=60, pady=10)

btnEliminarT = tk.Button(
    menu, text="Eliminar Término", bg="#F2B705", fg="#F2F2F2", 
    font=("Roboto", 12, "bold")
)
btnEliminarT.pack(fill="both", expand=True, padx=60, pady=11)

btnBuscarT = tk.Button(
    menu, text="Buscar Término", bg="#F2B705", fg="#F2F2F2", 
    font=("Roboto", 12, "bold")
)
btnBuscarT.pack(fill="both", expand=True, padx=60, pady=11)

btnListarT = tk.Button(
    menu, text="Listar Término", bg="#F2B705", fg="#F2F2F2", 
    font=("Roboto", 12, "bold")
)
btnListarT.pack(fill="both", expand=True, padx=60, pady=11)


# ------------------------------------------------------
# Sección "Agregar Término"
# ------------------------------------------------------

agregarTermino = tk.Frame(vn)


# ------------------------------------------------------
# Footer
# ------------------------------------------------------

footer = tk.Frame(vn)
footer.pack(fill="x", pady=(15, 0))

btnAcercaDe = tk.Button(
    footer, text="Acerca De", bg="#d91f2b", fg="#F2F2F2", 
    font=("Roboto", 12, "bold")
)
btnAcercaDe.pack(pady=10, padx=15, side="right")

btnSalir = tk.Button(
    footer, text="Salir", bg="#d91f2b", fg="#F2F2F2", 
    font=("Roboto", 12, "bold"), command=cerrarVentana
)
btnSalir.pack(pady=10, padx=15, side="left")


# ------------------------------------------------------
# Ejecutar la aplicación
# ------------------------------------------------------

vn.mainloop()
