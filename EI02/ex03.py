notas = []

nAl = int(input("Insira a quantidade de alunos: "))
apr = 0
rep = 0
md1 = 0
md2 = 0
mdmd = 0

for x in range(nAl):

    aluno = []

    aluno.append(input("Insira o nome do aluno %d: " % (x + 1)))

    nota = -1

    while nota < 0 or nota > 100:
        nota = int(input("Insira a primeira nota do aluno %d: " % (x + 1)))

    md1 += nota
    aluno.append(nota)

    nota = -1

    while nota < 0 or nota > 100:
        nota = int(input("Insira a segunda nota do aluno %d: " % (x + 1)))

    md2 += nota
    aluno.append(nota)

    md = (aluno[1] + aluno[2])/2

    mdmd += md
    aluno.append(md)

    if aluno[3] >= 60:
        aluno.append("Aprovado")
        apr += 1
    else:
        aluno.append("Reprovado")
        rep += 1

    print("\nNome do aluno: %s" % aluno[0])
    print("Nota 1: %d" % aluno[1])
    print("Nota 2: %d" % aluno[2])
    print("Média de notas: %d" % aluno[3])
    print("Situação: %s\n" % aluno[4])

print("Alunos aprovados: %d" % apr)
print("Alunos reprovados: %d" % rep)
print("Percentual de alunos aprovados: %.2f%%" % ((apr/nAl)*100))
print("Percentual de alunos reprovados: %.2f%%" % ((rep/nAl)*100))
print("Média da nota 1: %.2f" % (md1 / nAl))
print("Média da nota 2: %.2f" % (md2 / nAl))
print("Média das médias das notas: %.2f\n" % (mdmd / nAl))