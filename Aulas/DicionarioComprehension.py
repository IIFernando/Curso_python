# Dictionary Comprehesion and SET Comprehension.

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor
    for chave, valor
    in produto.items()
}

# Aqui um exemplo de SET Comprehension
s1 = {i for i in range(10)}
print(s1)