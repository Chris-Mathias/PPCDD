n = 1
d = {}

while n > 0:

    n = int(input("Insira um valor inteiro: "))

    if n > 0:

        if d.get(n) == None:
            d[n] = 1
        else:
            d[n] += 1

dlist = list(d.items())

print()

for x in dlist:
    print("O valor %d foi digitado %d vez(es)\n" % (x[0], x[1]))