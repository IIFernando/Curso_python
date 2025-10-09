'''
dir, hasattr e getattr em python

dir - Traz todos os métodos definidos no meu objeto.
hasattr - Checa se o objeto tem um método especifico.
getattr - Pode coletar o método definido a uma variavel.
'''

# DIR
string = 'Fernando'
print(dir(string))

# HASATTR
if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper())

# GETATTR
metodo = 'lower'
if hasattr(string, 'metodo'):
    print(f'Existe {metodo}')
    print(getattr(string, metodo)())
else:
    print(f'Não existe o método {metodo}')
