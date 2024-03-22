#Problema 2  / 7 ptos x4 pruebas / 28 puntos
#Ingreso de valores en árbol TRI-nario
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios números y cree un árbol trinario con listas
# esto es igual que el binario, pero los elementos que son iguales van en una lista
# centro, de la forma [numero, [subarbol IZQ], [mismo NUM], [subarbol DER] ]
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 30 90 90 8 5 90
#La salida debe ser
#         [20, [8, [5, [], [], []], [], []], [], [30, [], [], [90, [], [90, [], [90, [], [], []], []], []]]]
def arbolTrinario(numero):
    return [numero, [], [], []]

def insertaEnArbolTrinario(arbol, numero):
    if arbol == []:
        arbol += arbolTrinario(numero)
    elif numero < arbol[0]:
        insertaEnArbolTrinario(arbol[1], numero)
    elif numero == arbol[0]:
        arbol[2].append(numero)
    else:
        insertaEnArbolTrinario(arbol[3], numero)

def estaEnArbolTrinario(arbol, numero):
    if arbol == []:
        return False
    elif numero == arbol[0]:
        return True
    elif numero < arbol[0]:
        return estaEnArbolTrinario(arbol[1], numero)
    else:
        return estaEnArbolTrinario(arbol[3], numero)

def imprimirArbolTrinario(arbol):
    if arbol:
        print("[", arbol[0], end="")
        if arbol[1] or arbol[2] or arbol[3]:
            print(", ", end="")
        imprimirArbolTrinario(arbol[1])
        if arbol[2]:
            print(", [", end="")
            for i in range(len(arbol[2])):
                if i > 0:
                    print(", ", end="")
                print(arbol[2][i], end="")
            print("]", end="")
        if arbol[3]:
            print(", ", end="")
            imprimirArbolTrinario(arbol[3])
        print("]", end="")


if __name__ == "__main__":
    numeros = input().split()
    arbol_trinario = []
    for num in numeros:
        insertaEnArbolTrinario(arbol_trinario, int(num))
    imprimirArbolTrinario(arbol_trinario)

