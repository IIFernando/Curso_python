class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # Definição dos métodos da minha classe
    def buzinar(self):
        print('plim plim')

    def parar(self):
        print('Bicicleta padara.')

    def correr(self):
        print('Vrummmm.')

b1 = Bicicleta('Vermelha', 'Caloi', 2022, 600)
b1.parar()
# b1.correr()
# b1.buzinar()
print(b1.cor)

b2 = Bicicleta('Azul', 'Monark', 2000, 180)
print(b2.cor)