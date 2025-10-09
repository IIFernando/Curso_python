while True:

    def calculator(opcao, numero1, numero2):
        if opcao == 1:
            result = numero1 + numero2
            return result
        elif opcao == 2:
            result = numero1 - numero2
            return result
        elif opcao == 3:
            result = numero1 * numero2
            return result
        elif opcao == 4:
            result = numero1 / numero2
            return result

    print('Qual operação desejá executar? \n' +
          'Soma [1] \n' +
          'Subtração [2] \n' +
          'Multiplicação [3] \n' +
          'Divisão [4] \n' +
          'Sair [5] \n')

    op = int(input('Informe a operação que deseja executar: '))

    if op == 5:
        print('Calculadora encerrada.')
        break
    else:
        print('Opção errada! Tente novamente.')

    n1 = int(input('Informe o primeiro numero: '))
    n2 = int(input('Informe o segundo numero: '))

    print(f'O calculo entre {n1} e {n2} é {calculator(op, n1, n2)}')
