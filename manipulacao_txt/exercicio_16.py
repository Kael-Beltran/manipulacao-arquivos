def buscar_produto():

    with open("produtos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Teclado;120.50;10\n")
        arquivo.write("Mouse;75.90;15\n")
        arquivo.write("Monitor;899.90;5\n")
        arquivo.write("Headset;150.00;8\n")
        arquivo.write("Webcam;210.00;4\n")

    produtos = []

    with open("produtos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, preco, quantidade = linha.strip().split(";")

            produto = {
                "nome": nome,
                "preco": float(preco),
                "quantidade": int(quantidade)
            }

            produtos.append(produto)

    nome_pesquisar = input("Digite o produto: ")

    encontrado = False

    for produto in produtos:
        if produto["nome"].lower() == nome_pesquisar.lower():
            print("Produto encontrado!")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print(f"Quantidade: {produto['quantidade']}")
            encontrado = True

    if not encontrado:
        print("Produto não encontrado!")


buscar_produto()