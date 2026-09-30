def separar_numeros():

    with open("numeros.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("12\n")
        arquivo.write("7\n")
        arquivo.write("25\n")
        arquivo.write("30\n")
        arquivo.write("41\n")
        arquivo.write("56\n")
        arquivo.write("63\n")
        arquivo.write("72\n")
        arquivo.write("89\n")
        arquivo.write("90\n")

    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        numeros = [int(numero.strip()) for numero in arquivo]

    pares = []
    impares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    print("Números pares:")
    print(pares)

    print("Números ímpares:")
    print(impares)

separar_numeros()