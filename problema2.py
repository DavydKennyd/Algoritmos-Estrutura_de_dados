### INVERTER A STRING "ABELHA", OU SEJA "AHLEBA" FAZER ALGORITMO PARA FAZER ISSO 

string = "Abelha"
pilha = []

for letra in string:
    pilha.append(letra)
    print(pilha)
palavra_volta = ""
while pilha:
    palavra_volta = palavra_volta + pilha.pop()

print(palavra_volta) 


