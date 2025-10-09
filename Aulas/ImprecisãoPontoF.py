"""
    Imprecisão do ponto flutuante
"""
import decimal

numero_1 = decimal.Decimal('0.1') #usar o decimal em casos que a conta precise ser exata
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))