# O que é uma tupla? Estrutura excluiva da linguagem python. É uma lista que possui tamanho quase infinito, porém todos os dados ali contidos são imutáveis.

devedores = ("Amandah", "Ruan", "Ítalo", "Camila", "Stephany", "Algeice", "Hayde")
# Para as informações serem localizadas cada informação possui um índice.

usuario_vaiNoBanco = ()

usuario_vaiNoBanco = list(usuario_vaiNoBanco)

usuario_vaiNoBanco.append("Camila")

# print(usuario_vaiNoBanco)

usuario_vaiNoBanco = tuple(usuario_vaiNoBanco)

# lista / array:
cliente = ["Thamyres França", 123456789912, "30/10/2001"]


# Funções em Python

# As responsáveis por executarem determinadas partes de um código, tornando-o muito mais limpo r reutilizável

# projetando calculadora:
def calculo_soma(num1, sinal, num2):
  num1 = int(input("Digite o primeiro número: "))
  num2 = int(input("Digite o segundo número: "))
  sinal = input("Digite o sinal da sua operação matemática")
  if sinal == "+":
    print(f"O resultado da soma é {num1 + num2}")



def calculo_subtração(num1, num2):
  return num1 - num2

# Quando utilizamos o return estamos enviado o dado para algum lugar

guardar_calculo = calculo_subtração(10, 5)

print(guardar_calculo)