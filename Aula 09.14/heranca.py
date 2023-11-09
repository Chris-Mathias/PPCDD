class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return "Nome: " + self.nome + "\nIdade: " + str(self.idade)

    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade

class Aluno(Pessoa):

    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
    
    def getMatricula(self):
        return self.matricula
    
class Professor(Pessoa):

    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    
    def getSalario(self):
        return self.salario
    
a = Aluno("Paula", 30, 123)
print(a)

p = Professor("João", 40, 10000)
print(p)
