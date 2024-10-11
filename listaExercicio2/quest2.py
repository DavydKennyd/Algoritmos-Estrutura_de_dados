from binarytree import bst, build, Node 


no = bst(height=4)



def verificar_folha_no(no):
    if no is None:
        return 0 
    
    if no.left is None and no.right is None:
        return 1
    return verificar_folha_no(no.left) + verificar_folha_no(no.right)


contagem = verificar_folha_no(no)

print('Arvore: ')
print(no)
print("Contagem de nos: ", contagem)