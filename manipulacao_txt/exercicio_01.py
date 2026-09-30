# Modo "r" - Abre o arquivo para leitura
# Modo "x" - Cria um arquivo novo e gera erro se ele já existir

def ler_arquivo():
    with open("mensagem.txt", "x") as arquivo:
        arquivo.write("Olá Mundo!\n")
        arquivo.write("Estou aprendendo python\n")
        arquivo.write("Estou estudando manipulação de arquivos.\n")

    with open("mensagem.txt", "r") as arquivo:
        conteudo = arquivo.read()

        print(conteudo)

ler_arquivo()