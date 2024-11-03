import tkinter as tk 

# Funciones:

def cerrarVentana():
    vn.destroy()




vn = tk.Tk()
vn.configure(bg="#F2F2F2")
vn.geometry("600x420")
vn.resizable(False,False)
vn.title("Diccionario del Programador")
vn.iconbitmap("ui\img\diccionarioimg.ico")

nav = tk.Frame(vn)
nav.configure(bg="#D92534",width=600,height=42)
nav.pack(fill="x")

lbnav = tk.Label(nav,text="Diccionario Del Programador",font=("Roboto",24,"bold"),fg="#F2F2F2",bg="#D92534")
lbnav.pack(side="top")

instr = tk.Frame(vn)
instr.configure(height=67)
instr.pack(fill="x")

lbInstr = tk.Label(instr,text="Ingresa una Opcion:",font=("Roboto",16,"bold"),fg="#1B1259")
lbInstr.pack(side="top",anchor="s",pady=15)

menu = tk.Frame(vn)
menu.configure(width=270,height=220,bg="#1B1259")
menu.pack(side="top")

btnAgregarT = tk.Button(menu,text="Agregar Termino",bg="#FFCE00",fg="#F2F2F2",font=("Roboto",12,"bold"))
btnAgregarT.pack(fill="both",expand=True,padx=60,pady=10)

btnEliminarT = tk.Button(menu,text="Eliminar Termino",bg="#FFCE00",fg="#F2F2F2",font=("Roboto",12,"bold"))
btnEliminarT.pack(fill="both",expand=True,padx=60,pady=11)

btnBuscarT = tk.Button(menu,text="Buscar Termino",bg="#FFCE00",fg="#F2F2F2",font=("Roboto",12,"bold"))
btnBuscarT.pack(fill="both",expand=True,padx=60,pady=11)

btnListarT = tk.Button(menu,text="Listar Termino",bg="#FFCE00",fg="#F2F2F2",font=("Roboto",12,"bold"))
btnListarT.pack(fill="both",expand=True,padx=60,pady=11)

footer = tk.Frame(vn)
footer.pack(fill="x")

btnAcercaDe = tk.Button(footer,text="Acerca De",bg="#FFCE00",fg="#F2F2F2",font=("Roboto",12,"bold"))
btnAcercaDe.pack(pady=10)

btnSalir = tk.Button(footer,text="Salir",bg="#FFCE00",fg="#F2F2F2",font=("Roboto",12,"bold"),command=cerrarVentana)
btnSalir.pack(pady=10)

vn.mainloop()