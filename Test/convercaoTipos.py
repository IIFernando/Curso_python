# Conversão de tipos

preco = 10.50
idade = 28

#Forma de converter um valor para texto
print(str(preco)) 
print(str(idade))
print(int(preco)) #A conversão de um tipo float para inteiro pode ocorrer, porem se perde o valor após o ponto flutuante.
print(5 // 2)

#É possivel tambem converter as variaveis usando f-strings.
texto = f'idade {idade} preço {preco}'
print(texto)