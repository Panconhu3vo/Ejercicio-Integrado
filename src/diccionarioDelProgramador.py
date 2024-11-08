from diccionario import diccionario
if __name__ == "__main__":
    # Código de prueba o inicialización que no quieres que se ejecute en otros archivos
    print("Ejecutando diccionarioDelProgramador directamente")
# Zona de Variables
menu = ''' 
1: Agregar un término
2: Eliminar un término
3: Buscar traducción de un término
4: Mostrar todos los términos
5: Acerca De
6: Salir
''' # Varibale Del Menu
opc = 0 # Variable de opcion
llavesTemporales = []
noEncontrado = True
nombreLimpio = ""

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
                    print("Asegurate de escibir bien el termino")
                    n = input(">> ")
                elif noEncontrado == True:
                    return n
        
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






# Menu:
while True:
    print(menu)
    opc = int(input(">> "))
    if opc == 1:

        print("ingresa el nombre del termino que desea agregar ")
        terminoNuevo = input(">> ")
        print("ingresa la definicion del termino ")
        definicion = input(">> ")
        print("ingresa la traduccion del termino ")
        traduccion = input(">> ")

    elif opc == 2:
        print("Eliminar Termino")
    


    elif opc == 3:
        print("Buscar Termino")
        print("Ingresa el nombre del termino (Minuscula):")
        nombreTermino = input(">> ")
        nombreLimpio = verificarNombre(nombreTermino) 
        print(" ", nombreLimpio)
        print("     Definicion: ",diccionario[buscarTermino(nombreLimpio)][nombreLimpio]["definicion"])
        print("     Traduccion: ",diccionario[buscarTermino(nombreLimpio)][nombreLimpio]["traduccion"])
        print("     Categoria: ",diccionario[buscarTermino(nombreLimpio)][nombreLimpio]["categoria"])

        
    # elif opc == 4:
    # elif opc == 5:
    # elif opc == 6:
    # else: