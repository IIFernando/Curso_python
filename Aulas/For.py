'''
Iterável -> str, range, etc
iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
'''

numeros = range(0, 10)

for numero in numeros:
    if numero == 2:
        print('i é 2, pulando')
        continue

    if numero == 8:
        print('i é 8, seu ELSE não executará.')
        break

    for j in range(1, 3):
        print(numero, j)

else:
    print('For completo com sucesso.')