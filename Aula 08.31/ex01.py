gabaritotxt = open("/media/chris/SSD/Documentos/Python/PPCDD/Aula 08.31/gabarito.txt", "r") # substitua o caminho pelo desejado
gabarito = gabaritotxt.read().lower().split("-")

for x in gabarito:
    if x != "a" and x != "b" and x != "c" and x != "d" and x != "e":
        print("\nGabarito Inválido. Alternativas inexistentes\n")
        exit()

respostastxt = open("/media/chris/SSD/Documentos/Python/PPCDD/Aula 08.31/respostas.txt", "r") # substitua o caminho pelo desejado

resp = (str(respostastxt.read()).split("\n"))

respostas = []

for x in resp:
    s = x.split(";")

    if len(s) != 3:
        print("\nRespostas Inválidas. Modelo não Seguido\n")
        exit()
    
    s[1] = s[1].lower().split("-")
    
    if len(s[1]) != len(gabarito):
        print("\nRespostas Inválidas. Tamanho não corresponde ao gabarito\n")
        exit()

    for y in s[1]:
        if y != "a" and y != "b" and y != "c" and y != "d" and y != "e":
            print("\nRespostas Inválidas. Alternativas inexistentes\n")
            exit()

    respostas.append(s)

resultadotxt = open("/media/chris/SSD/Documentos/Python/PPCDD/Aula 08.31/resultado.txt", "w") # substitua o caminho pelo desejado

for x in respostas:
    respaluno = x[1]
    acertos = 0

    for i in range(len(respaluno)):
        if respaluno[i] == gabarito[i]:
            acertos += 1

    resultadotxt.write(x[0])
    resultadotxt.write(";")

    for y in range(len(x[1])-1):
        resultadotxt.write(x[1][y].upper())
        resultadotxt.write("-")

    resultadotxt.write(x[1][len(x[1])-1].upper())
    resultadotxt.write(";")
    resultadotxt.write(str(acertos))
    resultadotxt.write(";\n")

print("\nResultados gerados com sucesso!\n")