from diccionario import diccionario
# Zona de Variables
menu = ''' 
1: Agregar un término
2: Eliminar un término
3: Buscar traducción de un término
4: Mostrar todos los términos
5: Acerca De
6: Salir
''' # Varibale Del Menu
opc = 0 # Variable de Opcion
llavesTemporales = []
noEncontrado = True
nombreLimpio = ""
# ---
# Agregar Termino():


# ---
# Eliminar Término():


# ---
# Buscar Término():
def buscarTermino(termino):
    primeraPalabra = termino[0]
    return primeraPalabra
    
    



# ---
# Mostrar Términos():


# ---
# eliminarEspacios()
def eliminarEspacios(limpiarPalabra):
    terminoSinEspacios = limpiarPalabra.replace(" ", "")
    return terminoSinEspacios

def verificarNombre(n):
    noEncontrado = False
    m = eliminarEspacios(n)
    llavesTemporales = list(diccionario[buscarTermino(n)].keys())
    while noEncontrado == False:
                m = eliminarEspacios(n)
                for i in llavesTemporales:
                    if i == m:
                        noEncontrado = True
                        break
                    else:
                        noEncontrado = False
                if noEncontrado == False:
                    print("Asegurate de escibir bien el termino y que si exita:")
                    n = input(">> ")
                elif noEncontrado == True:
                    return n
                    break
        
# ---





# Menu:
while True:
    print(menu)
    opc = int(input(">> "))
    if opc == 1:
        print("Agregar Termino")
    elif opc == 2:
        print("Eliminar Termino")
    elif opc == 3:
        print("Buscar Termino")
        print("Ingresa el nombre del termino (Minuscula):")
        nombreTermino = input(">> ")
        nombreLimpio = verificarNombre(nombreTermino) 

        print("| ", nombreLimpio.ljust(165), " |")
        print("| Definicion:".ljust(83)," | ", "Traduccion:".ljust(80)," |" )
        print("| ",diccionario[buscarTermino(nombreLimpio)][nombreLimpio]["definicion"].ljust(80)," | ",diccionario[buscarTermino(nombreLimpio)][nombreLimpio]["traduccion"].ljust(80)," |")
        
    # elif opc == 4:
    # elif opc == 5:
    # elif opc == 6:
    # else: