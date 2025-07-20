'''
    Tîpos built-in do python são:

Texto - STR
Númerico - int, float, complex
Sequencia - list, tuple, range
Mapa - dict
Coleção - set, fronzenset
Booleano - bool
Binário - bytes, bytearray, memoryview
'''

age = 35 # Tipo inteiro.
name = 'Fernando' #Tipo string
WAGE = 5110.23 #Tipo float, constantes em python são declaradas com letras maíusculas.
count = 0


#Tipo MAP ou dicionário
curiosidades = {
    'Jogo Favorito': 'Resident Evil 4',
    'Altura': 1.85,
    'Comida': 'Batata-Frita'
}

print(f'Seu nome é {name} e você tem {age}, hoje seu salário atual é de {WAGE}')

if age >= 18: #Alguns tipos tambem pode ser usados para uma operação booleana de verdadeiro ou falso
    print('Você é maior de idade!')
else:
    print('Você é menor de idade')

#Um for para pegar o item de cada chave
for chave, valor in curiosidades.items():
    print(f"{chave}: {valor}")
