print("PRIMEIRA QUESTÃO")
alunos = {}

alunos["João"] = 8.5
alunos["Pedro"] = 7.5
alunos["Maria"] =  9.0
alunos["Ana"] = 8.7

nota_de_maria = alunos["Maria"]
print(f"A nota de Maria é {nota_de_maria}")



##EXERCICIO 2
print("SEGUNDA QUESTÃO")
alunos["Pedro"] = 8.0
print(f'Essa é a nova nota de pedro {alunos["Pedro"]}')

###EXERCICIO 3
print('TERCEIRA QUESTÃO')
del alunos["João"];

print(f"Esse foram os alunos que sobraram {alunos}")

####EXERCICIO 4
print('QUESTÃO QUATRO')
for aluno, nota in alunos.items():
    print(f'{aluno}: {nota}')

print('QUESTÃO CINCO')
print("Ana" in alunos); ##A SAÍDA IRA SER FALSE

##QUESTÃO SEIS
print('QUESTÃO SEIS')
print('Essa são a quantidades de pessoas no dicionario:', len(alunos))

###QUESTÃO SETE
print('QUESTÃO SETE')

Produtos = {
    "P001": "Arroz",
    "P002": "Feijão",
    "P003": "Macarrão"
}

for codigos, nome in Produtos.items():
    print(f'nome do produto: {nome}, codigo {codigos}');

for codigos in Produtos.keys():
    print(f'Codigos de produto {codigos}'); 

for nomes in Produtos.values():
    print(f'Nomes dos produtos {nomes}'); 