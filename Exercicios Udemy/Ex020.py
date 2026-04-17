numero = int(input('Informe um numero: '))

try:
    if numero % 2 == 0:
        print('PAR')
    elif numero % 2 == 1:
        print('IMPAR')
except:
    print('Valor digitado invalido')