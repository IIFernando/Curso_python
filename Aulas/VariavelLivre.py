# Variaveis livres + nonlocal, se refere ao escopo chamado em python locals e globals

print(globals())

def fora(x):
    a = x # Está seria uma variavel livre.
    def dentro():
        # print(locals())
        print(dentro.__code__.co_freevars) #Comando para ver as variaveis livres.
        return a #Ela é considerada uma variavel livre pois está fora do escopo desta função.
    return dentro

dentro1 = fora(10) #E a ela pode ser atribuido qualquer valor.
dentro2 = fora(20)

print(dentro1(), dentro2())