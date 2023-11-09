import csv

class conta:

    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome
        self.saldo = 0

    def alterarNome(self, nome):
        self.nome = nome
    
    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def transferencia(self, valor, conta):
        self.saldo -= valor
        conta.saldo += valor

    def getPrintDados(self):
        print("Conta Corrente: {}\nNome: {}\nSaldo: {}\n".format(self.numero, self.nome, self.saldo))
        return self.numero, self.nome, self.saldo
    
c1 = conta(1, "Alíbio")
c2 = conta(2, "Edisvaldo")
c3 = conta(3, "Pedro")

c1.deposito(100)
c2.deposito(2000)
c3.deposito(350)

c2.transferencia(1000, c1)

c3.saque(100)

arq = open("/media/chris/SSD/Documentos/Python/PPCDD/Lista 4/Relatório.csv", "w") # substitua o caminho pelo desejado
w = csv.writer(arq)

w.writerow("Conta Corrente, Nome, Saldo".split(", "))

for i in (c1, c2, c3):
    w.writerow(i.getPrintDados())
