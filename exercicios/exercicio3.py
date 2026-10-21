import csv

def relatorio_treinador():

    nome = input("Digite o nome do treinador: ")

    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        treinadores = csv.DictReader(arquivo)

        encontrado = False

        for treinador in treinadores:

            if treinador["nome"].lower() == nome.lower():

                print("Treinador:", treinador["nome"])
                print("Região:", treinador["regiao"])
                print("Nível:", treinador["nivel"])

                encontrado = True

    if encontrado == False:
        print("Treinador não encontrado.")
        return

    print("\nPokémon:")

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        pokemons = csv.DictReader(arquivo)

        for pokemon in pokemons:

            if pokemon["treinador"].lower() == nome.lower():
                print(
                    "-",
                    pokemon["nome"],
                    "-",
                    pokemon["tipo"],
                    "- Nível",
                    pokemon["nivel"]
                )


def media_treinador():

    nome = input("Digite o nome do treinador: ")

    soma = 0
    quantidade = 0

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        pokemons = csv.DictReader(arquivo)

        for pokemon in pokemons:

            if pokemon["treinador"].lower() == nome.lower():
                soma += int(pokemon["nivel"])
                quantidade += 1

    if quantidade == 0:
        print("Nenhum Pokémon encontrado.")
    else:
        media = soma / quantidade
        print("Média:", media)

def media_tipo():

    tipo = input("Digite o tipo: ")

    soma = 0
    quantidade = 0

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        pokemons = csv.DictReader(arquivo)

        for pokemon in pokemons:

            if pokemon["tipo"].lower() == tipo.lower():
                soma += int(pokemon["nivel"])
                quantidade += 1

    if quantidade == 0:
        print("Nenhum Pokémon encontrado.")
    else:
        media = soma / quantidade
        print("Média:", media)

def quantidade_treinador():

    quantidade = {}

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        pokemons = csv.DictReader(arquivo)

        for pokemon in pokemons:

            treinador = pokemon["treinador"]

            if treinador not in quantidade:
                quantidade[treinador] = 0

            quantidade[treinador] += 1

    print(quantidade)

def quantidade_tipo():

    quantidade = {}

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        pokemons = csv.DictReader(arquivo)

        for pokemon in pokemons:

            tipo = pokemon["tipo"]

            if tipo not in quantidade:
                quantidade[tipo] = 0

            quantidade[tipo] += 1

    print(quantidade)

def nivel_acima():

    nivel = int(input("Digite o nível: "))

    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        treinadores = csv.DictReader(arquivo)

        for treinador in treinadores:

            if int(treinador["nivel"]) > nivel:
                print(treinador)

while True:

    print("\n===== RELATÓRIOS =====")
    print("1 - Relatório de um treinador")
    print("2 - Média de nível dos Pokémon de um treinador")
    print("3 - Média de nível dos Pokémon por tipo")
    print("4 - Quantidade de Pokémon por treinador")
    print("5 - Quantidade de Pokémon por tipo")
    print("6 - Treinadores com nível acima de um valor")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        relatorio_treinador()

    elif opcao == "2":
        media_treinador()

    elif opcao == "3":
        media_tipo()

    elif opcao == "4":
        quantidade_treinador()

    elif opcao == "5":
        quantidade_tipo()

    elif opcao == "6":
        nivel_acima()

    elif opcao == "7":
        break

    else:
        print("Opção inválida.")