# Seria basicamente para fixar um valor a função e poder usa-lo de forma fixa.

def soma(x, y):
    return x + y

def multiplicacao(x, y):
    return x * y

def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

soma_com_cinco = criar_funcao(soma, 5) # aqui está definido como o parametro X fixo em 5
multiplica_por_dez = criar_funcao(multiplicacao, 10)

print(soma_com_cinco(10)) # Nas chamadas passa apenas o outro paramentro mutavel Y nesse caso definido como 10.
print(multiplica_por_dez(5))