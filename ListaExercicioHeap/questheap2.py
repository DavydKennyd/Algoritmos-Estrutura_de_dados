import random
import heapq


numeros_aleatorios = [random.randint(1, 10000) for _ in range(30)]

heapq.heapify(numeros_aleatorios)

#ENCONTRAR O NUMERO K;
#VOU COLOCAR OS 10 PRIMEIROS NUMEROS MAIS ALTOS, POIS NA QUESTÃO NÃO ESPECIFICA QUANTOS NUMEROS ALTO DEVO COLOCAR;

#maior_preco = heapq.nlargest(10,numeros_aleatorios)
#print(f"Os preços mais altos registrados até agora são: ", maior_preco)

for n in range(len(numeros_aleatorios)):
    numeros_aleatorios[n] *= -1
print('Os preços da lista ficaram negativo')
print('Antes do heap: ', numeros_aleatorios)
heapq.heapify(numeros_aleatorios)
print('Após o heap: ', numeros_aleatorios)

for k in range(len(numeros_aleatorios)):
    numeros_aleatorios[k] *= -1
print('Os preços não são negativos mais, mas agora a ordem está do maior para o menor: ')

print(numeros_aleatorios)

print('Os maiores cinco são: ')
for i in range(5):
    print(numeros_aleatorios[i])
