class Funcionario:
    def __init__(self, staff_id, nome, cargo,salario):
        self.staff_id = staff_id
        self.nome  = nome
        self.cargo = cargo
        self.salario = salario
    def info(self):
        return f"Nome: {self.nome}, Cargo: {self.cargo}, Salario: {self.salario}"


class Gerente(Funcionario):
    def __init__(self, staff_id, nome, cargo, salario, setor):
        super().__init__(staff_id, nome, cargo, salario)
        self.setor = setor

    def info(self):
        return f"Nome: {self.nome}, Cargo: {self.cargo}, Salario: {self.salario}, Setor: {self.setor}"

    def promocao(self):
        self.salario += self.salario * 0.15




    




    