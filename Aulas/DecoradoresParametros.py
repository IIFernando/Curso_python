def decoradora(func):
    print('Decoradora 1')

    def aninhada(*args, **kwargs):
        print('Aninhada')
        res = func(*args, **kwargs)
    return aninhada


@decoradora
def soma(a, b):
    print('Soma')
    return a + b

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
