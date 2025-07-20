"""
Exercicio Unir Listas
Criar uma função zipper (Como zipper de roupas)
O trabalho dessa função será unir duas listas na ordem.
 Use todos os valores da menor lista.

 EX.:
 ['Salvador', 'Ubatuba', 'Belo Horizonte']
 ['BA', 'SP', 'MG', 'RJ']
"""

estados = ['Salvador', 'Ubatuba', 'Belo Horizonte']
uf = ['BA', 'SP', 'MG', 'RJ']

def zipper(lista1, lista2):
    tLista1 = len(lista1)
    tLista2 = len(lista2)
    
    difLista = tLista1 - tLista2
            
    if tLista1 > tLista2:
        lista1.pop()
        joinList = []
        
        for u, z in zip(lista1, lista2):
            joinList.append(u)
            joinList.append(z)

                
    else:
        joinList = []
        lista2.pop()
        for u, z in zip(lista1, lista2):
            joinList.append(u)
            joinList.append(z)

    return joinList

print(zipper(estados, uf))

