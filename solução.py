caracteres_abrindo = ('(','{','[')
caracteres_fechando = (')','}',']')

pilha = []

def validar_expressao(expressao):    
    for e in expressao:
        if e == '(' , '{', '[':
            pilha.append(e)

            

    