textoInicial = "Este é um texto de exemplo. Este texto serve para exemplificar a repetição de palavras. A repetição de palavras é importante para este exemplo."

def comprimir(texto):
    tabela = {}
    reduzido = ""

    textoList = textoInicial.split()
    for n in textoList:
        if n in tabela:
            reduzido = reduzido + f'{tabela[n]} '
        else:
            tabela[n] = len(tabela)
            reduzido = reduzido + f'{tabela[n]} '

    return tabela, reduzido

def descomprimir(tabela, texto):
    completo = ""

    #implemente o codigo aqui

    return completo

def imprimir(cabecalho, texto):
    print(f"###{cabecalho}###")
    print(f"Texto: {texto}")
    print(f"Tamanho: {len(texto)}")

imprimir("Texto completo", textoInicial)

tabela, reduzido = comprimir(textoInicial)

imprimir("Texto comprimido", reduzido)

restaurado = descomprimir(tabela, reduzido)

imprimir("Texto restaurado", restaurado)
