import tkinter as tk 

vn = tk.Tk()
vn.configure(bg="#F2F2F2")
vn.geometry("600x500")
vn.resizable(False,False)
vn.title("Diccionario del Programador")
vn.iconbitmap("ui\img\diccionarioimg.ico")

nav = tk.Frame(vn)
nav.configure(bg="#D92534",width=600,height=42)
nav.pack(fill="x")

lbnav = tk.Label(nav,text="Diccionario Del Programador",font=("Roboto",24,"bold"),fg="#FFCE00",bg="#D92534")
lbnav.pack(side="top")

vn.mainloop()

