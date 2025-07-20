'''
Iterando strings com while
'''

nome = input('Digite seu nome: ') #Iteráveis

indice = 0
novo_nome = ''

while indice < len(nome) :
    novo_nome += '*' + nome[indice]
    indice += 1

print(novo_nome + '*')