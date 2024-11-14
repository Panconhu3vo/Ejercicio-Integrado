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


#       f'''Termino: {termino}
#  Definicion: {diccionario[termino[0]][termino]["definicion"]}
# Traduccion: {diccionario[termino[0]][termino]["traduccion"]}
#  Categoria: {diccionario[termino[0]][termino]["categoria"]}
        
if __name__ == "__main__":
    print("a")