from binarytree import bst,build,Node

no = bst(height = 4)

print('Arvore exemplo para saber se é aceita como uma arvore BST: ')
print(no)

def arvoreCerta(no):
    def verificar_tree(node, min_value=float('-inf'), max_value=float('inf')):
        if node is None:
            return True
        if node.value <= min_value or node.value >= max_value:
            return False
        return (verificar_tree(node.left, min_value, max_value ) and 
                verificar_tree(node.right, node.value, max_value))
    return verificar_tree(no)

tree=arvoreCerta(no)

print(tree)

