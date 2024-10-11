
alunos = {}


for i in range(3):
    nota1 = int(input('Adicione a primeira nota do aluno: '))
    nota2 = int(input('Adcione a segunda nota do aluno: '))
    matricula = int(input('Informe a matricula do sujeito: '))
    alunos[matricula] = [nota1, nota2]


for matricula, notas in alunos.items():
    nota1, nota2 = notas
    multiplica1 = nota1 * 2 
    multiplica2 = nota2 * 3
    soma = multiplica1 + multiplica2

    media = soma / 5

    print(F'Aluno da matricula {matricula} sua media é {media}, massa?')