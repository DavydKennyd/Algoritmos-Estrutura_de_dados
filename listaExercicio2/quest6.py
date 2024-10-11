from binarytree import bst, build, Node

no = bst(height = 4)

def soma_td_nos(no):
        if no is None:
            return 0  
        
        return no.value + soma_td_nos(no.left) + soma_td_nos(no.right)
    
print("A bst completa: ")
print(no)

soma = soma_td_nos(no)

print("A soma de todos os nós é: ", soma)
