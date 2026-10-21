import csv


def carregar_treinadores():

    with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
        treinadores = list(csv.DictReader(arquivo))

    return treinadores


def carregar_pokemons():

    with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
        pokemons = list(csv.DictReader(arquivo))

    return pokemons


def listar_treinadores():

    treinadores = carregar_treinadores()

    for treinador in treinadores:
        print(treinador)


def consultar_equipe():

    nome = input("Digite o nome do treinador: ")

    treinadores = carregar_treinadores()
    pokemons = carregar_pokemons()

    for treinador in treinadores:

        if treinador["nome"].lower() == nome.lower():

            print("Treinador:", treinador["nome"])
            print("Região:", treinador["regiao"])
            print("Nível:", treinador["nivel"])

            print("\nPokémon:")

            numero = 1

            for pokemon in pokemons:

                if pokemon["treinador"].lower() == nome.lower():

                    print(
                        numero,
                        "-",
                        pokemon["nome"],
                        "-",
                        pokemon["tipo"],
                        "-",
                        pokemon["nivel"]
                    )

                    numero += 1

            return

    print("Treinador não encontrado.")


def calcular_pontuacao():

    treinadores = carregar_treinadores()
    pokemons = carregar_pokemons()

    resultados = []

    for treinador in treinadores:

        nome = treinador["nome"]

        soma = 0
        quantidade = 0

        for pokemon in pokemons:

            if pokemon["treinador"].lower() == nome.lower():

                soma += int(pokemon["nivel"])
                quantidade += 1

        pontuacao = int(treinador["nivel"]) + soma

        resultado = {
            "treinador": nome,
            "regiao": treinador["regiao"],
            "nivel_treinador": treinador["nivel"],
            "quantidade_pokemons": quantidade,
            "soma_niveis": soma,
            "pontuacao": pontuacao
        }

        resultados.append(resultado)

    return resultados


def mostrar_classificacao():

    resultados = calcular_pontuacao()

    # organiza do maior para o menor
    for i in range(len(resultados)):

        for j in range(i + 1, len(resultados)):

            if resultados[i]["pontuacao"] < resultados[j]["pontuacao"]:

                temp = resultados[i]
                resultados[i] = resultados[j]
                resultados[j] = temp

    numero = 1

    for resultado in resultados:

        print(
            numero,
            "-",
            resultado["treinador"],
            "-",
            resultado["pontuacao"],
            "pontos"
        )

        numero += 1


def gerar_csv():

    resultados = calcular_pontuacao()

    with open(
        "resultado_campeonato.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        campos = [
            "treinador",
            "regiao",
            "nivel_treinador",
            "quantidade_pokemons",
            "soma_niveis",
            "pontuacao"
        ]

        escritor = csv.DictWriter(
            arquivo,
            fieldnames=campos
        )

        escritor.writeheader()

        for resultado in resultados:
            escritor.writerow(resultado)

    print("Arquivo criado!")
    print("Quantidade de registros:", len(resultados))


while True:

    print("\n===== CAMPEONATO POKÉMON =====")
    print("1 - Listar treinadores")
    print("2 - Consultar equipe")
    print("3 - Calcular pontuação")
    print("4 - Mostrar classificação")
    print("5 - Gerar arquivo CSV")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_treinadores()

    elif opcao == "2":
        consultar_equipe()

    elif opcao == "3":

        resultados = calcular_pontuacao()

        for resultado in resultados:
            print(
                resultado["treinador"],
                "-",
                resultado["pontuacao"],
                "pontos"
            )

    elif opcao == "4":
        mostrar_classificacao()

    elif opcao == "5":
        gerar_csv()

    elif opcao == "6":
        break

    else:
        print("Opção inválida.")