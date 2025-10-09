# Empacotamento e desempacotamento de dicionários

# args e kwargs
# args -> Argumentos não nomeados
# kwargs -> Argumentos nomeados

def mostroArgumentos(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

a, b = 1 ,2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

a, b = pessoa.values()
print(a, b)

a, b = pessoa.items()
print(a, b)

mostroArgumentos(nome='Aline', sobrenome='Araujo')