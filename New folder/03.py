class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'{self.nome} tem {self.idade} anos'
class Aluno(Pessoa):
    def __init__(self, nome, idade, notas):
        super().__init__(nome, idade)
        self.notas = notas
    def __str__(self):
        return f'{self.nome} tem {self.idade} anos e suas notas são {self.notas}'
    




class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina
    def __str__(self):
        return f'{self.nome} tem {self.idade} anos e leciona {self.disciplina}'
    
    def colocar_nota(self, aluno, notas):
        aluno.notas = notas




aluno = Aluno("Joao", 20, 5)
professor = Professor("Mr Fiap", 40, "Bungee Jump")
professor.colocar_nota(aluno,10)
print(aluno)




