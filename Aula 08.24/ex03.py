x = []

for i in range(2):
    x.append(int(input("Insira um valor inteiro: ")))

x.sort()

if x[0] == x[1]:
    print("Números iguais")

else:
    print("O maior número é", x[1], "e a diferença entre eles é de", x[1] - x[0])
