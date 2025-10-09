'''Funções decoradoras e decoradores
Decorar = Adicionar / Remover / Restringir / Alterar
Funções decoradoras são utilizadas para decorar outras funções.
   Decoradores são usados para fazer o python usar as funções
decoradoras em outras funções.
 Decoradores no python são chamados de syntax sugar (açucar sintático).
'''
def criar_funcao(func):
    def interna(*args, **kargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kargs)
        print(f'O resultado foi {resultado}')
        print('OK, agora vai você foi decorada')
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    print(inverte_string.__name__)
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string.')



invertida = inverte_string('123')
# invertida = inverte_string('Fernando')
print(invertida)
