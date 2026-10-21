import csv

def listar_treinadores():
    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        treinadores = csv.DictReader(arquivo)

        for treinador in treinadores:
            print(treinador)

def buscar_treinador():
    nome = input("Digite o nome do treinador: ")

    encontrado = False

    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        treinadores = csv.DictReader(arquivo)

        for treinador in treinadores:
            if treinador["nome"].lower() == nome.lower():
                print(treinador)
                encontrado = True

    if encontrado == False:
        print("Treinador não encontrado.")

def buscar_regiao():
    regiao = input("Digite a região: ")

    encontrado = False

    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        treinadores = csv.DictReader(arquivo)

        for treinador in treinadores:
            if treinador["regiao"].lower() == regiao.lower():
                print(treinador)
                encontrado = True

    if encontrado == False:
        print("Nenhum treinador encontrado.")

def maior_nivel():
    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        treinadores = list(csv.DictReader(arquivo))

    maior = treinadores[0]

    for treinador in treinadores:
        if int(treinador["nivel"]) > int(maior["nivel"]):
            maior = treinador

    print(maior)

def menor_nivel():
    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        treinadores = list(csv.DictReader(arquivo))

    menor = treinadores[0]

    for treinador in treinadores:
        if int(treinador["nivel"]) < int(menor["nivel"]):
            menor = treinador

    print(menor)

while True:

    print("\n===== TREINADORES POKÉMON =====")
    print("1 - Listar todos os treinadores")
    print("2 - Buscar treinador pelo nome")
    print("3 - Listar treinadores de uma região")
    print("4 - Mostrar treinador com maior nível")
    print("5 - Mostrar treinador com menor nível")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_treinadores()

    elif opcao == "2":
        buscar_treinador()

    elif opcao == "3":
        buscar_regiao()

    elif opcao == "4":
        maior_nivel()

    elif opcao == "5":
        menor_nivel()

    elif opcao == "6":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")