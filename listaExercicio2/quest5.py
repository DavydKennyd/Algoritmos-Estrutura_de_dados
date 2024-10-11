from binarytree import bst, Node

raiz = bst(height=4)

def traversal(no):                                  
    if no is None:
        return
    
    fila = [no]  
    i = 0
    
    while i < len(fila):
        no_atual = fila[i]
        
        if no_atual is not None:
            print(no_atual.value, end=" ")
            fila.append(no_atual.left)  
            fila.append(no_atual.right)  
        
        i += 1


traversal(raiz)