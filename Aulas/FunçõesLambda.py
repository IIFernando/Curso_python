''''
 As funções lambda são como qualquer outra em python. Porém, são
funções anônimas que contém apenas uma linha. Ou seja, tudo deve
ser contido dentro de uma unica expressão.
'''

lista = [
    {'nome': 'Fernando', 'sobrenome': 'Araujo'},
    {'nome': 'Lavinia', 'sobrenome': 'Araujo'},
    {'nome': 'Matheus', 'sobrenome': 'Araujo'},
    {'nome': 'Bruna', 'sobrenome': 'Araujo'}
    ]

# def ordena(item):
#     return item['nome']

# lista.sort(key=ordena)
# lista.sort(key=lambda item: item['nome'])
#
# for item in lista:
#     print(item['nome'])

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(lambda x, y : x + y, 2, 3
            )
)