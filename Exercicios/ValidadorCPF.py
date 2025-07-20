"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

 Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

 Para calcular e segundo digito, é só acrescentar na
multiplicação o primeiro digito calculado.

"""

import re
import random

#Forma tradicional de limpar uma entrada do usuário usando replace
"""cpf = input('Digite o CPF para ser validado: ').replace('.', '') \
    .replace('-', '')"""

cpf = input('Digite o CPF para ser validado: ')
#Tratar o input com REGEX, expressões regulares.
cpfTratado = re.sub(
             r'[^0-9]',
             '',
                cpf)

nove_digitos = cpfTratado[:9]
contagem1 = 10
contagem2 = 10
soma1 = 0
soma2 = 0

for i, digito01 in enumerate(nove_digitos):
    digitoConv01 = int(digito01)
    resultado1 = digitoConv01 * contagem1
    contagem1 -= 1
    soma1 += resultado1

digito_1 = soma1 * 10

if digito_1 % 11 > 9:
    primeiroDigito = 0
else:
    primeiroDigito = digito_1 % 11

validacao02 = nove_digitos + str(primeiroDigito)

for i, digito02 in enumerate(validacao02):
    digitoConv02 = int(digito02)
    resultado2 = digitoConv02 * contagem2
    contagem2 -= 1
    soma2 += resultado2

digito_2 = soma2 * 10

if digito_2 % 11 > 9:
    segundoDigito = 0
else:
    segundoDigito = digito_2 % 11


cpfCompleto = nove_digitos + str(primeiroDigito) + str(segundoDigito)
if cpfCompleto == cpfTratado:
    print(f'CPF {cpfCompleto} validado com sucesso!')
else:
    print(f'CPF {cpfCompleto} inválido.')



