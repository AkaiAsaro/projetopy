tarefas = []


def add_tasks():
  while True:
    nome = input("digite a tarefa: ")
    if not nome.strip():
      print("tarefa não pode ser vazia")
      continue
    descrição = input("digite a descrição: ")
    if not descrição.strip():
      print("descrição necessaria")
      continue
    prioridade = input("digite a prioridade(baixa/media/alta): ")
    if prioridade not in ["baixa", "media", "alta"]:
      print("prioridade invalida")
      continue
    categoria = input("digite a categoria: ")
    if not categoria.strip():
      print("categoria necessaria")
      continue
    tarefa = {
    "nome": nome,
    "descrição": descrição,
    "prioridade": prioridade,
    "categoria": categoria,
    }
    tarefas.append(tarefa)
    print("tarefa adicionada com sucesso")
    return tarefas

def show_tasks():
  for i in range(len(tarefas)):
    print(f"\ntarefas: {tarefas[i]}")
