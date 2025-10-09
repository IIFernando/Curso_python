# Generator expression, Iterables e Iterator em python
# # Iteretor fornece uma maneira de acessar sequencialmente os elementos de um objeto agregado sem expor sua representação
# subjacente.

import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() # Tem __iter__ e __next__

lista = [n for n in range(1000000)] # criar um iterador com list comprehension, ele desteja todos os valores em memoria de uma vez
generator = (n for n in range(1000000)) # Já usando generators, precisamos chamar a posição para acessar seu valor (Função que pausa)

# print(sys.getsizeof(lista))
# print(sys.getsizeof(generator))

def generetor(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return

'''     
    yield 1 # yield pausa a função e tambe marmazena seu valor de retorno
    print('Continuando...')
    yield 2 # Outra pausa
    return 'ACABOU!
'''

gen = generetor(maximum=1000000)
for n in gen:
    print(n)
# print(next(gen))
# print(next(gen)) # Chama o proximo valor da função com next