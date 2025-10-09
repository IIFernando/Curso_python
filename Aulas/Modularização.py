'''
 Entendendo os seus próprios módulos Python
o primeiro módulo executado chama-se __main__
você pode importar outro módulo inteiro ou parte dele
o python conhece a pasta onde o __main__ está e as pastas
abaixo dele.
 Ele não reconhece pastas e módulos acima do __main__ por
padrão, o python conhece todos os módulos e pacotes presentes
nos caminhos de sys.path.
'''

# Forma de importar somente a função que preciso.
from Models.model import soma #Teste de uma importação de módulos criados.

# E a forma para importar todo o modulo tendo acesso a todas as funções
from Models import model 
import sys

import Models

print(soma(10, 5))
print(model.soma(25, 5))
print(Models.model.soma(50, 10))# Usando o init para importar a minha função de soma, essa forma engana o python fazendo ele achar que a pasta é um modulo nativo.
