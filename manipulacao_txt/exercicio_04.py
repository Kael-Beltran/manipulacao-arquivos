# Modo "r" - Abre o arquivo para leitura

def contar_linhas():
    quantidade = 0

    with open("nomes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            quantidade += 1

    print(f"O arquivo possui {quantidade} linhas.")

contar_linhas()