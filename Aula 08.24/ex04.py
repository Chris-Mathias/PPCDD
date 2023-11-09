gabarito = []
respostaAluno = []
numQuest = int(input("\nInsira o número de questões: "))
continuar = ""
acertos = 0

for i in range(numQuest):
    resposta = input("\nInsira a resposta da questão %d: " % (i + 1)).upper()

    while resposta not in ['A', 'B', 'C', 'D', 'E']:
        print("\nAlternativa inválida")
        resposta = input("\nInsira a resposta da questão %d: " % (i + 1)).upper()
        
    gabarito.append(resposta)

while continuar != "n":

    for i in range(numQuest):
        resposta = input("\nInsira a resposta do aluno da questão %d: " % (i + 1)).upper()

        while resposta not in ['A', 'B', 'C', 'D', 'E']:
            print("\nAlternativa inválida")
            resposta = input("\nInsira a resposta do aluno da questão %d: " % (i + 1)).upper()
            
        respostaAluno.append(resposta)

    for i in range(numQuest):

        if respostaAluno[i] == gabarito[i]:
            acertos += 1

    print("\nO aluno acertou %d questões" % (acertos))

    respostaAluno = []
    acertos = 0

    continuar = input("\nDeseja continuar corrigindo? (S/n) ").lower()
