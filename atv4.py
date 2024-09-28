####################
#
# Nome: Fábio Rian Rodrigues Maia
# Curso: P2 Informática
# Prof.: Allan Kelvin
#
####################

import random

palpites = []

mamíferos = {1: 'cachorro', 2: 'leão', 3: 'gato', 4: 'macaco', 5: 'cavalo', 6: 'urso'}
aves = {1: 'gaivota', 2: 'arara', 3: 'avestruz', 4: 'galinha', 5: 'águia', 6: 'canarinho'}
répteis = {1: 'lagarto', 2: 'jacaré', 3: 'crocodilo', 4: 'camaleão', 5: 'iguana', 6: 'cobra'}
peixes = {1: 'tilapia', 2: 'sardinha', 3: 'atum', 4: 'cará', 5: 'peixe', 6: 'baiacu'}
anfíbios = {1: 'sapo', 2: 'axolote', 3: 'rã', 4: 'salamandra', 5: 'tritão', 6: 'tartaruga'}
while True:
    opcao = int(input("Escolha uma categoria de animais: \n1-mamíferos\n2-aves\n3-répteis\n4-peixes\n5-anfíbios\n-> "))
    if opcao < 1:
      print("Erro")
    elif opcao > 5:
      print("Erro")
    else:
      break
if opcao == 1:
    num_random = random.choice(mamíferos)
if opcao == 2:
    num_random = random.choice(aves)
if opcao == 3:
    num_random = random.choice(répteis)
if opcao == 4:
    num_random = random.choice(peixes)
if opcao == 5:
    num_random = random.choice(anfíbios)
print("------- Vamos Iniciar o Jogo! --------------\n")
dica = len(num_random)
while True:
    print(f"Dica: A palavra tem {dica} letras")
    palpite = input("Tente adivinhar a palavra: ").lower()
    palpites.append(palpite)
    if palpite == num_random:
        break
    else:
        print("Palpite errado.")
        print("Tente novamente.\n")
        continue
print("Parabéns! Você acertou a palavra.")
print(f"Número de palpites: {len(palpites)}")
print(f"Palpites realizados: {palpites}")
