from binarytree import bst, Node

def alturaBST(no):
    if no is None:
        return 0
    return 1 + max(alturaBST(no.left), alturaBST(no.right))

def verificaBalanceada(no):
    if no is None:
        return True
    left_height = alturaBST(no.left)
    right_height = alturaBST(no.right)
    if abs(left_height - right_height) > 1:
        return False
    return verificaBalanceada(no.left) and verificaBalanceada(no.right)


arvore = bst(height=4)
print(arvore)
if verificaBalanceada(arvore):
    print("Está balanceada")
else:
    print("Não está balanceada")
