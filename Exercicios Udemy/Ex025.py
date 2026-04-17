'''
Faça jogo para o usuário adivinhar qual a palavra secreta. Você vai propor uma palavra secreta qualquer e vai dar a
possibilidade para o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.

- Se a letra digitada estiver na palavra secreta; exiba a letra.
- Se a letra digitada não estiver na palavra secreta; exiba *.
- Fazer a contagem de tentativas.
'''

palavra = 'fernando'

acerto = 0
erro = 0

while True:

    letra = input('Digite uma letra: ')

    if letra in palavra:
        acerto += 1
        print(f'Você acertou a letra {letra} faz parte da palavra secreta. Acertos N° {acerto}.')
    elif letra not in palavra:
        erro += 1
        print(f'Infelizmente a letra {letra} não faz parte da palavra secreta. Erros {erro}.')

    if acerto == len(palavra):
        print(f'Parabens você acertou todas as letras com um numero total de {acerto + erro} tentativas, a palavra secreta é {palavra}')
        break

    while True:
        resp = input('Deseja continuar? [s/n] ')
        if resp == 's':
            break
        elif resp == 'n':
            break
        else:
            print('Opção inválida. Tente novamente.')

    if resp == 'n':
        print('Você desistiu!!!')
        break