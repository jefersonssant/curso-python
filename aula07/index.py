# Funções --> Organizar melhor o código, reutilizar códigos, esperar uma ação, executar blocos de códigos.

def lista_compras():
  print("Comprar leite em pó")

# lista_compras()

# login = input("Digite seu e-mail: ")
# senha = int(input("Digite sua Senha:" ))

# def boas_vindas():
  # print(f"Boas vindas, {login} aproveite que nosso site está em promoção de 50% do valor do frente")

# def login_invalido():
  # print("Tente novamente, suas credenciais estão inválidas")

# if login == "email@provedor.com" and senha == 123:
  # boas_vindas()
# else:
  # login_invalido()

# Dicionários em Python

# () tuplas -> Quando queremos guardar informações que não podem ser modificadas.

# [] listas / arrays -> Quando queremos guardar uma quantidade quase infinita de informação, porém não organizada.

# {} Dicionários -> Quando queremos guardar uma quantidade quase infinita de informação, de forma organizada (organizado em prateleiras)

nomes_cliente = {
  'cliente_rj': 'Kauã',
  'cliente_mg': ['Alisson', 'Isael'],
  'cliente_pb': 'Haydée',
  'cliente_pe': 'Nat',
  'cliente_ba': 'Jeferson',
  'cliente_sp': 'Leandra',
  'cliente_df': 'Karyne',
  'cliente_al': 'Camila',
  'cliente_ce': 'Renato',
  'cliente_se': 'Évila',
}

# Cada chave deve ser única, não pode ter chaves repetidas.

print(nomes_cliente)

# Alterar uma informação de um dicionário

# nomes_cliente['cliente_rj'] = "Mariana" -> Aqui substitui

# Adicionar uma nova chave e valor

# nomes_cliente.update({'cliente_são_gonçalo': 'Mariana'})

# deletar uma informação no dicionário

# del nomes_cliente['cliente_al']

# Adicionando informação em uma chave que tem uma lista:

nomes_cliente['cliente_mg'].append('Mônica')

# for fofoqueiro in local:

for clientes in nomes_cliente.values():
  print(clientes)