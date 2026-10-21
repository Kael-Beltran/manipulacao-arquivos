import csv


def listar_treinadores():

    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        treinadores = csv.DictReader(arquivo)

        for treinador in treinadores:
            print(treinador["nome"])


def gerar_treinador():

    nome = input("Digite o treinador: ")

    encontrados = []

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        pokemons = csv.DictReader(arquivo)

        for pokemon in pokemons:

            if pokemon["treinador"].lower() == nome.lower():
                encontrados.append(pokemon)

    if len(encontrados) == 0:
        print("Nenhum Pokémon encontrado.")
        return

    nome_arquivo = "pokemons_" + nome.lower().replace(" ", "_") + ".csv"

    with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:

        campos = ["nome", "tipo", "nivel", "treinador"]

        escritor = csv.DictWriter(
            arquivo,
            fieldnames=campos
        )

        escritor.writeheader()

        for pokemon in encontrados:
            escritor.writerow(pokemon)

    print("Arquivo criado!")
    print("Quantidade:", len(encontrados))


def gerar_todos():

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        pokemons = list(csv.DictReader(arquivo))

    # organiza manualmente pelo nível
    for i in range(len(pokemons)):

        for j in range(i + 1, len(pokemons)):

            if int(pokemons[i]["nivel"]) > int(pokemons[j]["nivel"]):

                temp = pokemons[i]
                pokemons[i] = pokemons[j]
                pokemons[j] = temp

    with open(
        "todos_pokemons_ordenados.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        campos = ["nome", "tipo", "nivel", "treinador"]

        escritor = csv.DictWriter(
            arquivo,
            fieldnames=campos
        )

        escritor.writeheader()

        for pokemon in pokemons:
            escritor.writerow(pokemon)

    print("Arquivo criado!")
    print("Quantidade:", len(pokemons))


while True:

    print("\n===== GERADOR DE ARQUIVOS =====")
    print("1 - Listar treinadores")
    print("2 - Gerar CSV de um treinador")
    print("3 - Gerar CSV de todos os treinadores")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_treinadores()

    elif opcao == "2":
        gerar_treinador()

    elif opcao == "3":
        gerar_todos()

    elif opcao == "4":
        break

    else:
        print("Opção inválida.")