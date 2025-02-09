print("Bem vindo ao Vai No Lanche")

pedidos = []

qntd_pedidos = int(input("Boa noite, caro cliente, quantos pedidos deseja fazer: "))

while len(pedidos) < qntd_pedidos:
  pedidos.append(input(f"Digite o seu{len(pedidos)+1}º pedido: "))

print(f"Os seus pedidos foram{pedidos} em até uma hora chegarão a sua residência")
