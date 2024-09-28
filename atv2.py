####################
#
# Nome: Fábio Rian Rodrigues Maia
# Curso: P2 Informática
# Prof.: Allan Kelvin
#
####################

onibus = {
    1: "disponível",
    2: "disponível",
    3: "disponível",
    4: "disponível",
    5: "disponível"
}
assentos = 0

print("=====RESERVA DE ASSENTOS=====")

while True:
    if onibus == {}:
        break
    print(f"Assentos disponíveis: {list(onibus.keys())}")
    assentos = int(input("Deseja reservar qual assento? "))
    if assentos not in onibus:
        print(f"O assento {assentos} está ocupado ou não existe")
        continue
    else:
        print(f"Assento {assentos} reservado!")    
        print("-"*37)
    onibus.pop(assentos)

print("\nTodos os assentos foram reservados!")
