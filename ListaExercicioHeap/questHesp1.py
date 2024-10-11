import random 
import heapq

numeros_aleatorios = [random.randint(1, 10000) for _ in range(1000)]


heapq.heapify(numeros_aleatorios)

for n in range(5):
        menor = heapq.heappop(numeros_aleatorios)
        print(menor)
        
        


        