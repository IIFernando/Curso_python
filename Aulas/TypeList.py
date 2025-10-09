"""
Listas em python
Tipo list - Mutável
suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - -indices e fatiamento
Métodos úteis:
    append - Adicionar elemento no final da lista
    insert - Adicionar elemento no índice escolhido
    pop - Remover elemento no final da lista ou do índice escolhido
    del - Remove elemento
    clear - Limpa a lista
    extend - estende a lista de elementos
    (+ -) - concatena listas

Create Read Update Delete
Criar, Ler, alterar, apagar = lista[i] (CRUD)
"""

string = 'ABCDE' # 5 CARACTERES
#Índices  0     1       2         3
lista = [123, True, 'Fernando', 1.2]
lista2 = ['Matheus', 'Bruna']
print(lista, type(lista))

lista[1] = False
del lista[3]
lista.append(50) #Adiciona um item ao fim da lista
print(lista, type(lista))
lista.pop() #Remove um item ao fim da lista
print(lista, type(lista))
lista.insert(10, 'Lavínia') #Com e INSERT podemos passar o indice de onde queremos inserir o dado.
print(lista, type(lista))

lista.extend(lista2)  # método extendi mexe diretamente na lista em que ele for chamado, não precisando atribuir a uma nova lista
print(lista, type(lista))

for i in lista:
    print(i)