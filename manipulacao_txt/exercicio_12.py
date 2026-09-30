def classificar_alunos():

    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana;8.5\n")
        arquivo.write("Bruno;5.0\n")
        arquivo.write("Carlos;7.2\n")
        arquivo.write("Daniela;9.0\n")
        arquivo.write("Eduardo;3.5\n")
        arquivo.write("Fernanda;6.8\n")
        arquivo.write("Gabriel;2.0\n")

    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        alunos = [linha.strip() for linha in arquivo]

    for aluno in alunos:
        nome, nota = aluno.split(";")
        nota = float(nota)

        if nota >= 6:
            situacao = "Aprovado"
        elif nota >= 4:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"

        print(f"{nome} - {nota} - {situacao}")

classificar_alunos()