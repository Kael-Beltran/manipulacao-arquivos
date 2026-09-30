# Modo "w" - Abre para escrita e apaga o conteúdo existente

def criar_arquivo():
    with open("frase.txt", "w", encoding="utf-8") as arquivo:
        frase = input("Digite uma frase: ")

    with open("frase.txt", "w+", encoding="utf-8") as arquivo:
        arquivo.write(frase)

        print(frase)

criar_arquivo()