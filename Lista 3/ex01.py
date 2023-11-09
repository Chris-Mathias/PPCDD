import json

arq = open("/media/chris/SSD/Documentos/Python/PPCDD/Lista 3/Gabarito.json", "r") # substitua o caminho pelo desejado

gabaritojson = json.load(arq)
gabarito = {}
alunos = {}
resultados = {}

# Para cada questão no gabarito, adiciona a resposta ao dicionário
for i in gabaritojson["gabarito"]:

    # Verifica se a resposta é válida
    if i["resposta"].lower() not in ["a", "b", "c", "d", "e"]:
        print("Resposta %s inválida" % i["resposta"])
        exit(1)

    gabarito[i["questao"]] = i["resposta"]

# Para cada aluno no gabarito, adiciona o seu nome e as suas respostas ao dicionário
for i in gabaritojson["alunos"]:
    gabaritoaluno = {}

    for j in i["respostas"]:

        # Verifica se a questão existe no gabarito e se a resposta é válida
        if j["questao"] not in gabarito:
            print("Questão %d não existe no gabarito" % j["questao"])
            exit(1)
        if j["resposta"].lower() not in ["a", "b", "c", "d", "e"]:
            print("Resposta %s inválida" % j["resposta"])
            exit(1)

        gabaritoaluno[j["questao"]] = j["resposta"]
        
    alunos[i["nome"]] = gabaritoaluno

# Para cada aluno, verifica quantas questões ele acertou
for i in alunos:

    acertos = 0

    for j in alunos[i]:
        
        # Se a resposta do aluno for igual ao gabarito, adiciona um acerto
        if alunos[i][j].lower() == gabarito[j].lower():
            acertos += 1

    resultados[i] = acertos

print(gabarito)
print(alunos)

with open("/media/chris/SSD/Documentos/Python/PPCDD/Lista 3/Resultados.json", "w") as res: # substitua o caminho pelo desejado
    json.dump(resultados, res, indent=4)
