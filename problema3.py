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
def insert_trinary(root, num):
    if not root:
        return [num, [], [], []]
    if num < root[0]:
        root[1] = insert_trinary(root[1], num)
    elif num == root[0]:
        if not root[2]:
            root[2] = []
        root[2].append(num)
    else:
        root[3] = insert_trinary(root[3], num)
    return root

def construct_trinary_tree(numbers):
    numbers = numbers.split()
    valid_numbers = []
    for num in numbers:
        num = ''.join(filter(str.isdigit, num))
        if num:
            valid_numbers.append(int(num))
    root = None
    for num in valid_numbers:
        root = insert_trinary(root, num)
    return root

def print_trinary_tree(root):
    if not root:
        return
    print("[", root[0], end="")
    if root[1] or root[2] or root[3]:
        print(", ", end="")
    print_trinary_tree(root[1])
    if root[2]:
        print(", ", root[2], end="")
    if root[3]:
        print(", ", end="")
        print_trinary_tree(root[3])
    print("]", end="")

if __name__ == "__main__":
    numbers = input()
    trinary_tree = construct_trinary_tree(numbers)
    print_trinary_tree(trinary_tree)
