# Mapeamento de dados com list comprehension

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novo_produto = [
    {**produto, 'preco': produto['preco']* 1.05}
    if produto['preco'] >= 20 else {**produto} and produto['preco'] * 1.05 > 10 # Este pode ser considerado um tipo de filter
    for produto in produtos
]

# List comprehension com mais de um for
lista = []

for x in range(3):
    for y in range(0, 3):
        lista.append((x, y))

lista2 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista2)