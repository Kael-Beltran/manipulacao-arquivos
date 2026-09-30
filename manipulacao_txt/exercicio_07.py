def buscar_nome():

    with open("nomes.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana\n")
        arquivo.write("Bruno\n")
        arquivo.write("Carlos\n")
        arquivo.write("Daniela\n")
        arquivo.write("Eduardo\n")
        arquivo.write("Fernanda\n")
        arquivo.write("Gabriel\n")

    with open("nomes.txt", "r", encoding="utf-8") as arquivo:
        nomes = [nome.strip() for nome in arquivo]

    nome_pesquisar = input("Digite o nome que deseja pesquisar: ")

    if nome_pesquisar in nomes:
        print("Nome encontrado!")
    else:
        print("Nome não encontrado!")

buscar_nome()