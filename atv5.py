####################
#
# Nome: Fábio Rian Rodrigues Maia
# Curso: P2 Informática
# Prof.: Allan Kelvin
#
####################

def adicionar_tarefa(lista_tarefas):
  tarefas = input("\nDigite a tarefa que deseja adicionar: ")
  while True:
    prioridades = input("Digite a prioridade da tarefa (baixa/média/alta): \n").lower()
    if prioridades in ["baixa", "média", "alta"]:
      break
    else:
      print("Prioridade inválida.\n")
  lista_tarefas.append({"tarefa": tarefas, "prioridade": prioridades})

def exibir_tarefas(lista_tarefas):
  if len(lista_tarefas) > 0:
    print("\nTarefas de prioridade alta:")
    for t, tarefa in enumerate(lista_tarefas):
      if tarefa["prioridade"] == "alta":
        print(f"[{t+1}] Tarefa: {tarefa['tarefa']} - Prioridade: {tarefa['prioridade']}")

    print("\nTarefas de prioridade média:")
    for t, tarefa in enumerate(lista_tarefas):
      if tarefa["prioridade"] == "média":
        print(f"[{t+1}] Tarefa: {tarefa['tarefa']} - Prioridade: {tarefa['prioridade']}")

    print("\nTarefas de prioridade baixa:")
    for t, tarefa in enumerate(lista_tarefas):
      if tarefa["prioridade"] == "baixa":
        print(f"[{t+1}] Tarefa: {tarefa['tarefa']} - Prioridade: {tarefa['prioridade']}")
  else:
    print("Não há tarefas cadastradas.\n")

def concluir_tarefa(lista_tarefas):
  tarefa_concluir = int(input("Digite o número da tarefa para concluir: "))
  if tarefa_concluir >= 1 and tarefa_concluir <= len(lista_tarefas):
    lista_tarefas.pop(tarefa_concluir - 1)
    print("Tarefa concluída com sucesso!\n")
  else:
    print("Número de tarefa inválido.\n")

lista_tarefas = []
prioridades = ""
tarefas = ""
opcao = 0

print("=====GERENCIADOR DE TAREFAS=====")
while True:
  print("\nEscolha uma opção:")
  print("1-Adicionar tarefa")
  print("2-Exibir tarefas")
  print("3-Concluir tarefa")
  print("4-Sair")
  opcao = int(input("Opção: "))
  if opcao == 1:
    adicionar_tarefa(lista_tarefas)
  elif opcao == 2:
    exibir_tarefas(lista_tarefas)
  elif opcao == 3:
    concluir_tarefa(lista_tarefas)
  elif opcao == 4:
    print("Saindo do programa...")
    break
  else:
    print("Opção inválida. Tente novamente.\n")
