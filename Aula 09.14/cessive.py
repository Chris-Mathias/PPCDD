import csv

lista = [["nome","idade"],
         ["João",30],
         ["Maria",25]]

arq = open("/media/chris/SSD/Documentos/Python/PPCDD/Aula 09.14/teste.csv")
arq2 = open("/media/chris/SSD/Documentos/Python/PPCDD/Aula 09.14/novo.csv", "w")
dados = csv.reader(arq)
w = csv.writer(arq2)

print(dados)
print(type(dados))
print()

for item in dados:
    print(item)
    print(type(item))

for i in lista:
    w.writerow(i)

arq.close()
arq2.close()