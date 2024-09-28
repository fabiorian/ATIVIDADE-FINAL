####################
#
# Nome: Fábio Rian Rodrigues Maia
# Curso: P2 Informática
# Prof.: Allan Kelvin
#
####################

temperaturas = []
abaixo_da_media = []

print("=====TEMPERATURAS DIÁRIAS=====")
for i in range(10):
  while True:
    temp = float(input(f"Digite a temperatura do {i + 1}º dia: "))
    if 15 <= temp <= 40:
      temperaturas.append(temp)
      break
    else:
      print("Valor inválido, digite uma temperatura entre 15 e 40 graus.")


temp_media = sum(temperaturas) / len(temperaturas)

for temp in temperaturas:
  if temp < temp_media:
    abaixo_da_media.append(temp)

print("\n=====TEMPERATURAS=====")
print(f"Menor temperatura: {min(temperaturas)}°C")
print(f"Maior temperatura: {max(temperaturas)}°C")
print(f"Temperatura média: {temp_media}°C")
print(f"Dias que a temperatura média: {len(abaixo_da_media)}")
