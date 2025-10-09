"""
Introdução ao desempacotamento e empacotamento + tuples (Tuplas)
"""

nomes = ['Bruna', 'Fernando', 'Lavinia', ' Matheus']
"""
 É possivel desempacotar conforme abaixo em variaveis atribuindo a lista, ou poderia ser diretamente na lista \
daria tambem para ignorar posições na lista usando o '_' como uma posição de váriavel
"""
_, nome1, *_ = nomes
print(nome1)