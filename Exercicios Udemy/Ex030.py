import copy

# Exercícios

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# For para atualizar o valor
for produto in produtos:

    # Alterar apenas o preço e tambem ajusta para 2 casas decimais no dicionário.
    if 'preco' in produto:
        produto['preco'] = round(produto['preco'] * 1.10, 2)


# Criação do novo dicionário com cópia profunda
novos_produtos = copy.deepcopy(produtos)

# Ordene os produtos por nome decrescente (do maior para menor)
nome_desc = sorted(produtos, key=lambda x: x['nome'], reverse=True) # Ordenação tanto de nome quanto de preço crescente e decrescente usando função lambda e o metodo sorted

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(produtos, key=lambda x: x['nome'])
# Ordene os produtos por preco crescente (do menor para maior)
preco_desc = sorted(produtos, key=lambda x: x['preco'])
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
Produtos_ordenados_por_preco = copy.deepcopy(novos_produtos)
preco_asce = sorted(produtos, key=lambda x: x['preco'])

# FOR apenas para passar a lista
for produto in preco_asce:
    print(produto)