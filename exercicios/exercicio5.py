import csv


def carregar_pokemons():

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        pokemons = list(leitor)

    return pokemons


def listar(pokemons):

    for pokemon in pokemons:
        print(pokemon)


def pesquisar(pokemons):

    nome = input("Digite o nome do Pokémon: ")

    for pokemon in pokemons:

        if pokemon["nome"].lower() == nome.lower():
            print(pokemon)
            return

    print("Pokémon não encontrado.")


def adicionar(pokemons):

    nome = input("Nome: ")
    tipo = input("Tipo: ")
    nivel = input("Nível: ")
    treinador = input("Treinador: ")

    if nome == "":
        print("Nome não pode ficar vazio.")
        return

    if tipo == "":
        print("Tipo não pode ficar vazio.")
        return

    if treinador == "":
        print("Treinador não pode ficar vazio.")
        return

    nivel = int(nivel)

    if nivel < 1 or nivel > 100:
        print("O nível deve estar entre 1 e 100.")
        return

    for pokemon in pokemons:

        if pokemon["nome"].lower() == nome.lower():
            print("Pokémon já existe.")
            return

    novo = {
        "nome": nome,
        "tipo": tipo,
        "nivel": str(nivel),
        "treinador": treinador
    }

    pokemons.append(novo)

    print("Pokémon adicionado.")


def alterar(pokemons):

    nome = input("Digite o nome do Pokémon: ")
    nivel = int(input("Digite o novo nível: "))

    for pokemon in pokemons:

        if pokemon["nome"].lower() == nome.lower():

            pokemon["nivel"] = str(nivel)

            print("Nível alterado.")
            return

    print("Pokémon não encontrado.")


def remover(pokemons):

    nome = input("Digite o nome do Pokémon: ")

    for pokemon in pokemons:

        if pokemon["nome"].lower() == nome.lower():

            pokemons.remove(pokemon)

            print("Pokémon removido.")
            return

    print("Pokémon não encontrado.")


def salvar(pokemons):

    with open(
        "pokemons_atualizados.csv",
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

    print("Alterações salvas.")


pokemons = carregar_pokemons()


while True:

    print("\n===== GERENCIADOR DE POKÉMON =====")
    print("1 - Listar Pokémon")
    print("2 - Pesquisar Pokémon")
    print("3 - Adicionar Pokémon")
    print("4 - Alterar nível de um Pokémon")
    print("5 - Remover Pokémon")
    print("6 - Salvar alterações")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar(pokemons)

    elif opcao == "2":
        pesquisar(pokemons)

    elif opcao == "3":
        adicionar(pokemons)

    elif opcao == "4":
        alterar(pokemons)

    elif opcao == "5":
        remover(pokemons)

    elif opcao == "6":
        salvar(pokemons)

    elif opcao == "7":
        break

    else:
        print("Opção inválida.")