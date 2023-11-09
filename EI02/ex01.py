f1 = set()
f2 = set()
continuar1 = ""
continuar2 = ""

while continuar1 != "n":

    f1.add(str(input("Insira o nome de uma fruta para o conjunto 1: ")))

    continuar1 = str(input("Deseja continuar? (S/n) ")).lower()

while continuar2 != "n":

    f2.add(str(input("Insira o nome de uma fruta para o conjunto 2: ")))

    continuar2 = str(input("Deseja continuar? (S/n) ")).lower()

uni = f1 | f2
inter = f1 & f2
dif1 = f1 - f2
dif2 = f2 - f1

if len(f1) < len(f2):
    dif = len(f2) - len(f1)

elif len(f1) > len(f2):
    dif = len(f1) - len(f2)

else:
    dif = 0

print("\nA união dos conjuntos de frutas é:", uni, "\n")
print("A interseção dos conjuntos de frutas é:", inter, "\n")

if dif1 != set():
    print("A diferença entre os conjuntos 1 e 2 é:", dif1, "\n")
else:
    print("A diferença entre os conjuntos 1 e 2 é um conjunto vazio\n")

if dif2 != set():
    print("A diferença entre os conjuntos 2 e 1 é:", dif2, "\n")
else:
    print("A diferença entre os conjuntos 2 e 1 é um conjunto vazio\n")

print("A diferença de tamanhos entre os dois conjuntos é", dif, "\n")