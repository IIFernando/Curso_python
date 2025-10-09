'''
Introdução ao try/except e finally
try -> tentar executar um bloco de código
except -> ocorreu algum erro ao tentar executar
'''

'''
numero = input ('Vou dobrar o número que você digitar: ')

try:
    # Conversão de tipo de uma variavel
    numeroFloat = float(numero) 
    print(f'O dobro de {numero} é {numeroFloat * 2:.2f}')
except ValueError:
    print('Isso não é um número.')'''
    
'''
try:
    a = 18
    b = 0
    print('Linha 1'[50])
    div = a / b
    print('Linha 2')
    
except ZeroDivisionError:
    print(f'Erro divisão por {b} impossivel')
except NameError:
    print('Nome B não está definido')
except (TypeError, IndexError) as error: # Aqui podemos definir uma instancia para a classe de erro, a ver a sua MSG espeficica.
    print(f'MSG - {error.__class__.__name__}')
except Exception:
    print('Erro desconhecido.')
'''

try:
    print('1')
    # 8/0
except ZeroDivisionError: # É possivel ter quantos except for preciso para tratar as excessões.
    print('Não é possivel dividir por zero')
else: # Tambem é possivel incluior um else, caso o bloco try de certo ele tambem será executado.
    print('Não deu erro!')
finally: # O parametro finally sempre será executado ao ser incluido no bloco try.
    print('2')