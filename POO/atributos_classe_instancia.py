class Estudante:
    escola = 'DIO' #Exemplo de uma variavel de classe.

    #Definição do construtor.
    def __init__(self, nome, matricula):
        self.nome = nome #Exemplo de uma variavel de instância.
        self.matricula = matricula

    def __str__(self) -> str:
        return f'{self.nome} - {self.matricula} - {self.escola}'
    
aluno01 = Estudante('Fernando', 7)

# print(aluno01)


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod #Transforme em um método de classe, e nesse caso não utilizamos mais self e sim cls que referencia o método da classe.
    def criar_pessoa(cls , ano, mes, dia, nome):
        idade = 2026 - ano
        return cls(nome, idade)
    
    #Instansiação de um método estatico na classe.
    @staticmethod
    def maior_idade(idade):
        return idade >= 18

# p = Pessoa('Fernando', 37)

p = Pessoa.criar_pessoa(1989, 3, 9, "Fernando")
print(p.nome, p.idade, Pessoa.maior_idade(p.idade))


