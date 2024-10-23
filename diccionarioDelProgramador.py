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
abcdario = "abcdefghijklmnopqrstuvwxyz"
comienzo = 0
# ---
# Agregar Termino():


# ---
# Eliminar Término():


# ---
# Buscar Término():
def buscarTermino(x):
    
    for i in range(abcdario):
        if abcdario[i] == x[0]:
            comienzo = i
    print(i)


# ---
# Mostrar Términos():


# ---


# Menu:
while True:
    print(menu)
    opc = int(input(">>"))
    if opc == 1:
    
    # elif opc == 2:
    # elif opc == 3:
    # elif opc == 4:
    # elif opc == 5:
    # elif opc == 6:
    # else: