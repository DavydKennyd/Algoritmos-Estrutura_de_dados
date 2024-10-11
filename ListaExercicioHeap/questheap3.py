import heapq


fila_de_prioridade = []


def adicionar_tarefa(fila,prioridade, tarefa):
    heapq.heappush(fila,(prioridade, tarefa))


def remover_tarefa_com_maior_prioridade(fila):
    if fila:
        prioridade,tarefa = heapq.heappop(fila)
        return tarefa
    else:
        return None
    

adicionar_tarefa(fila_de_prioridade, 1, "Tarefa Urgente")
adicionar_tarefa(fila_de_prioridade, 5, "Tarefa Menos Importante")
adicionar_tarefa(fila_de_prioridade, 3, "Tarefa Normal")

tarefa = remover_tarefa_com_maior_prioridade(fila_de_prioridade)
print(f"Tarefa de maior prioridade removida: {tarefa}")