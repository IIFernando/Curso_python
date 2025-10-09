'''
Flag (Bandeira) - Marcar um local
Nome = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
'''

condicao = True
passou = None

if condicao:
    passou = True
    print('Faça algo')
else:
    print('Não faça algo')

print(passou, passou is None)
print(passou, passou is not None)