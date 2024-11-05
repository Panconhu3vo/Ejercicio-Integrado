import tkinter as tk 

# Funciones:

def cerrarVentana():
    vn.destroy()

def volver():
    nav.pack(fill="x")
    instr.pack(fill="x")
    menu.pack(side="top")
    footer.pack(fill="x")
    nav2.pack_forget()
    agregarTermino.pack_forget()
    

def seccionAT():
    agregarTermino.pack(fill="both")
    nav2.pack(fill="x")
    nav.pack_forget()
    instr.pack_forget()
    menu.pack_forget()
    footer.pack_forget()




vn = tk.Tk()
vn.configure(bg="#F2F2F2")
vn.geometry("600x420")
vn.resizable(False,False)
vn.title("Diccionario del Programador")
vn.iconbitmap("ui\img\diccionarioimg.ico")

nav = tk.Frame(vn)
nav.configure(bg="#1B1259",width=600,height=42)
nav.pack(fill="x")

lbnav = tk.Label(nav,text="Diccionario Del Programador",font=("Roboto",22,"bold"),fg="#F2F2F2",bg="#1B1259")
lbnav.pack(side="top")

nav2 = tk.Frame(vn)
nav2.configure(bg="#D92534",width=600,height=42)

lbnav2 = tk.Label(nav2, text="Diccionario Del Programador", font=("Roboto", 22, "bold"), fg="#F2F2F2", bg="#D92534")
lbnav2.pack(side="left", padx=(10, 0)) 

btnVolver = tk.Button(nav2, text="Volver", bg="#FFCE00", fg="#F2F2F2", font=("Roboto", 12, "bold"), command=volver)
btnVolver.pack(side="right", padx=(0, 10), pady=5)

instr = tk.Frame(vn)
instr.configure(height=67)
instr.pack(fill="x")

lbInstr = tk.Label(instr,text="Ingresa una Opcion:",font=("Roboto",16,"bold"),fg="#D92534")
lbInstr.pack(side="top",anchor="s",pady=15)

menu = tk.Frame(vn)
menu.configure(width=270,height=220,bg="#1B1259")
menu.pack(side="top")

btnAgregarT = tk.Button(menu,text="Agregar Termino",bg="#F2F2F2",fg="#211261",font=("Roboto",12,"bold"),command=seccionAT)
btnAgregarT.pack(fill="both",expand=True,padx=60,pady=10)

agregarTermino = tk.Frame(vn)


btnEliminarT = tk.Button(menu,text="Eliminar Termino",bg="#F2B705",fg="#F2F2F2",font=("Roboto",12,"bold"))
btnEliminarT.pack(fill="both",expand=True,padx=60,pady=11)

btnBuscarT = tk.Button(menu,text="Buscar Termino",bg="#F2B705",fg="#F2F2F2",font=("Roboto",12,"bold"))
btnBuscarT.pack(fill="both",expand=True,padx=60,pady=11)

btnListarT = tk.Button(menu,text="Listar Termino",bg="#F2B705",fg="#F2F2F2",font=("Roboto",12,"bold"))
btnListarT.pack(fill="both",expand=True,padx=60,pady=11)

footer = tk.Frame(vn)
footer.pack(fill="x")

btnAcercaDe = tk.Button(footer,text="Acerca De",bg="#F2B705",fg="#F2F2F2",font=("Roboto",12,"bold"))
btnAcercaDe.pack(pady=10)

btnSalir = tk.Button(footer,text="Salir",bg="#F2B705",fg="#F2F2F2",font=("Roboto",12,"bold"),command=cerrarVentana)
btnSalir.pack(pady=10,padx=10,side="left")


vn.mainloop()