def gerar_relatorio():

    with open("vendas.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana;Notebook;3500.00\n")
        arquivo.write("Bruno;Mouse;80.00\n")
        arquivo.write("Carlos;Teclado;150.00\n")
        arquivo.write("Ana;Monitor;900.00\n")
        arquivo.write("Daniela;Notebook;3500.00\n")
        arquivo.write("Bruno;Headset;200.00\n")
        arquivo.write("Carlos;Mouse;80.00\n")
        arquivo.write("Ana;Teclado;150.00\n")
        arquivo.write("Daniela;Monitor;900.00\n")

    vendas = []

    with open("vendas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            vendedor, produto, valor = linha.strip().split(";")

            venda = {
                "vendedor": vendedor,
                "produto": produto,
                "valor": float(valor)
            }

            vendas.append(venda)

    print("VENDAS:")

    for venda in vendas:
        print(f"{venda['vendedor']} - {venda['produto']} - R$ {venda['valor']:.2f}")

    total = 0

    for venda in vendas:
        total = total + venda["valor"]

    print(f"\nTOTAL DE VENDAS: R$ {total:.2f}")

    quantidade_vendas = {}

    for venda in vendas:
        vendedor = venda["vendedor"]

        if vendedor in quantidade_vendas:
            quantidade_vendas[vendedor] = quantidade_vendas[vendedor] + 1
        else:
            quantidade_vendas[vendedor] = 1

    print("\nQuantidade de vendas:")

    for vendedor in quantidade_vendas:
        print(f"{vendedor}: {quantidade_vendas[vendedor]}")

    total_vendedor = {}

    for venda in vendas:
        vendedor = venda["vendedor"]

        if vendedor in total_vendedor:
            total_vendedor[vendedor] = total_vendedor[vendedor] + venda["valor"]
        else:
            total_vendedor[vendedor] = venda["valor"]

    maior_vendedor = ""
    maior_valor = 0

    for vendedor in total_vendedor:
        if total_vendedor[vendedor] > maior_valor:
            maior_valor = total_vendedor[vendedor]
            maior_vendedor = vendedor

    print(f"\nMaior valor em vendas: {maior_vendedor} - R$ {maior_valor:.2f}")


gerar_relatorio()