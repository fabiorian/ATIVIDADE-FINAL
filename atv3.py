####################
#
# Nome: Fábio Rian Rodrigues Maia
# Curso: P2 Informática
# Prof.: Allan Kelvin
#
####################

import time

def adicionar_funcionario(funcionarios):
  nome = input("\nDigite o nome do funcionário: ")
  idade = int(input("Digite a idade do funcionário: "))
  cargo = input("Digite o cargo do funcionário: ").lower()
  funcionarios.append({"nome": nome, "idade": idade, "cargo": cargo})
  print("\nFuncionário adicionado com sucesso!")

def listar_funcionarios(funcionarios):
  for func in funcionarios:
    print(f"Nome: {func['nome']}, Idade: {func['idade']}, Cargo: {func['cargo']}")

def buscar_por_cargos(funcionarios, buscar_cargo):
  funcionarios2 = []
  buscar_cargo = input("Digite o cargo que deseja buscar: ").lower()
  for funcio in funcionarios:
    if funcio['cargo'] == buscar_cargo:
      funcionarios2.append(funcio)
    if not funcionarios2:
      print(f"Nenhum funcionário encontrado com o cargo {buscar_cargo}.")
    else:
      print(f"Funcionários encontrados com o cargo {buscar_cargo}:")
      for funcio in funcionarios2:
        print(f"Nome: {funcio['nome']}, Idade: {funcio['idade']}")
  return funcionarios2

nome = ""
idade = 0
cargo = ""
funcionarios = []
buscar_cargo = ""

print("=====SISTEMA DE CADASTRO DE FUNCIONÁRIOS=====")
while True:
  print("1-Adicionar funcionário")
  print("2-Listar funcionários")
  print("3-Buscar funcionários por cargo")
  print("4-Sair")
  opcao = input("Opção: ")
  if opcao == "1":
    adicionar_funcionario(funcionarios)
  elif opcao == "2":
    listar_funcionarios(funcionarios)
  elif opcao == "3":
    buscar_por_cargos(funcionarios, buscar_cargo)
  elif opcao == "4":
    print("Saindo do sistema...")
    time.sleep(1)
    break
  else:
    print("Opção inválida. Tente novamente.\n")
