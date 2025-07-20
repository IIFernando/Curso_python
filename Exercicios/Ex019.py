nome = input('Informe seu nome: ')
idade = input('Informe sua idade: ')


if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Se nome contem espaços: {' ' in nome}')
    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[len(nome) - 1]}')
else:
    print('Desculpe, você deixou campos vazios.')