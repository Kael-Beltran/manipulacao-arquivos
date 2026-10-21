import csv


def listar_pokemons():
    nome = input("Digite o nome do treinador: ")

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        pokemons = csv.DictReader(arquivo)

        encontrados = []

        for pokemon in pokemons:
            if pokemon["treinador"].lower() == nome.lower():
                encontrados.append(pokemon)

        if len(encontrados) == 0:
            print("Nenhum Pokémon encontrado.")

        else:
            for pokemon in encontrados:
                print(pokemon)


def contar_pokemons():
    nome = input("Digite o nome do treinador: ")

    quantidade = 0

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        pokemons = csv.DictReader(arquivo)

        for pokemon in pokemons:
            if pokemon["treinador"].lower() == nome.lower():
                quantidade += 1

    print("Quantidade de Pokémon:", quantidade)


def maior_pokemon():
    nome = input("Digite o nome do treinador: ")

    maior = None

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        pokemons = csv.DictReader(arquivo)

        for pokemon in pokemons:

            if pokemon["treinador"].lower() == nome.lower():

                if maior is None:
                    maior = pokemon

                elif int(pokemon["nivel"]) > int(maior["nivel"]):
                    maior = pokemon

    if maior is None:
        print("Nenhum Pokémon encontrado.")
    else:
        print(maior)


def menor_pokemon():
    nome = input("Digite o nome do treinador: ")

    menor = None

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        pokemons = csv.DictReader(arquivo)

        for pokemon in pokemons:

            if pokemon["treinador"].lower() == nome.lower():

                if menor is None:
                    menor = pokemon

                elif int(pokemon["nivel"]) < int(menor["nivel"]):
                    menor = pokemon

    if menor is None:
        print("Nenhum Pokémon encontrado.")
    else:
        print(menor)


def buscar_tipo():
    tipo = input("Digite o tipo: ")

    encontrado = False

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        pokemons = csv.DictReader(arquivo)

        for pokemon in pokemons:
            if pokemon["tipo"].lower() == tipo.lower():
                print(pokemon)
                encontrado = True

    if encontrado == False:
        print("Nenhum Pokémon encontrado.")


while True:

    print("\n===== POKÉMON DOS TREINADORES =====")
    print("1 - Listar Pokémon de um treinador")
    print("2 - Contar Pokémon de um treinador")
    print("3 - Mostrar Pokémon de maior nível")
    print("4 - Mostrar Pokémon de menor nível")
    print("5 - Listar Pokémon de determinado tipo")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_pokemons()

    elif opcao == "2":
        contar_pokemons()

    elif opcao == "3":
        maior_pokemon()

    elif opcao == "4":
        menor_pokemon()

    elif opcao == "5":
        buscar_tipo()

    elif opcao == "6":
        break

    else:
        print("Opção inválida.")