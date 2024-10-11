from binarytree import bst, build, Node


no = bst(height=4)

def conta_no_interno(no):
    if no is None:
        return 0 
    if no.left is None and no.right is None:
        return 0
    return 1 + conta_no_interno(no.left) + conta_no_interno(no.right)

print("Arvore BST para contar o nó interno: ")
print(no)

numero = conta_no_interno(no)
print("Contagem dos nó internos: ", numero)