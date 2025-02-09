# Estruturas condicionais, repetição e manipulação de strings
#nome = 'Jeferson'
#print(f'Ola, {nome}')

#Condicionais --> Elas são responsáveis por executar um determinado bloco de código, baseado em um ou mais respostas específicas.
#Condicionais simples, compostas e aninhadas.

# Condicionais simples

saldo = False

if saldo == False:
  print(f'Tá lascado')

#Condicionais compostas

idade = 18

if saldo == True and idade >= 18:
  print(f'Uhuuuul, você pode mandar um pixa aos seus instrutores')
else:
  print(f'Infelizmente você não pode mandar pix para os seus instrutores')

# Condicionais aninhadas

jantar = 'Churrasco acompanhado de fritas e farofa'
bebida = 'Coca-cola'

if jantar == 'Churrasco acompanhado de fritas e farofa' and bebida == 'Coca-cola':
  print(f'Partiuuuu churrascadaaa!')
elif jantar == 'Strognoff de franco' and bebida == 'Coca-cola':
  print(f'Partiu comer Strogonoff')
else:
  print(f'Deixo pra próxima!')

# Operadores lógicos e Operadores de Comparação python

# JavaScript -> &, ||, !
# Python -> and, or, not