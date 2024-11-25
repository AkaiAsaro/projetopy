from functions.todolist import add_tasks,  show_tasks

while True:
  menu = input("""
  escolha o que deseja fazer
  1. adicionar tarefas
  2. exibir tarefas
  3. marcar tarefas
  0. sair
  """
)

  match menu:
    case "1":
      add_tasks()
    case "2":
      show_tasks()
    case "3":
      ...
    case "0":
      print("programa encerrado")
      break

