import json

arq = open("/media/chris/SSD/Documentos/Python/PPCDD/Aula 09.14/teste.json")
dados = json.load(arq)

print(dados)
print(type(dados))
print()

for item in dados:
    print(item)
    print(type(item))

    