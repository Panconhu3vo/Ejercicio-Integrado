from diccionario import diccionario

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






