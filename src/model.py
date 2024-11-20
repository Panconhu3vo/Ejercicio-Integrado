from diccionario import diccionario
'''
print(" ", nombreLimpio)
print("     Definicion: ",diccionario[buscarTermino(nombreLimpio)][nombreLimpio]["definicion"])
print("     Traduccion: ",diccionario[buscarTermino(nombreLimpio)][nombreLimpio]["traduccion"])
print("     Categoria: ",diccionario[buscarTermino(nombreLimpio)][nombreLimpio]["categoria"])
'''


def verificarNombre(termino):
    termino = " ".join(termino.split())
    termino = termino.lower()
    for i in "abcdefghijklmnopqrstuvwxyz":
        if termino in list(diccionario[i].keys()):
            return True
            break
    return False 

  


if __name__ == "__main__": 
    print((diccionario["a"].keys()))
    verificarNombre(input("> "))






