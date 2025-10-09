"""
 Introudu"cão a funções (def) em python
funcões são trechos de código usados para
replicar determinada ação ao longo do seu código
 Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
  Por padrão, funções python retornam None (nada)
"""

def Soma(x=None, y=None):

    if x is not None and y is not None:
        print(f'a soma de X e y é {x + y}')
    else:
        print('Um dos digitos não foi informado.')


"""
 Escopo de funcões em python
escopo significa o local onde aquele código pode atingir.
 Existe o escopo global e local
o escopo global é o escopo onde todo o código e alcançavel.
o escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
"""

def escopo():
    x = 1
    print(x)

escopo()