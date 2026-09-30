def mostrar_numeros():

    with open("numeros.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("10\n")
        arquivo.write("15\n")
        arquivo.write("22\n")
        arquivo.write("31\n")
        arquivo.write("40\n")
        arquivo.write("55\n")
        arquivo.write("68\n")
        arquivo.write("73\n")
        arquivo.write("80\n")
        arquivo.write("91\n")

    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        numeros = [int(numero.strip()) for numero in arquivo]

    for numero in numeros:
        if numero % 2 == 0:
            print(numero)

mostrar_numeros()