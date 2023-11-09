class Animal:

    def __init__(self):
        pass

    def locomove(self):
        pass

class Peixe(Animal):

    def locomove(self):
        print("Nadando")

class Elefante(Animal):

    def locomove(self):
        print("Andando")

class Passaro(Animal):

    def locomove(self):
        print("Voando")

peixe = Peixe()
passaro = Passaro()
elefante = Elefante()

for a in (peixe, passaro, elefante):
    a.locomove()