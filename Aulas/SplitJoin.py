"""
Split - Divide uma STRING
Join -  Une uma STRING
"""

frase = 'Olha só que, coisa interessante!'

lista = frase.split(',')
for i, valor in enumerate(lista):
    print(valor.strip())

novaFrase = ', '.join(lista)
print(novaFrase)