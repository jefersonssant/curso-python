# cadeado 13

#numeros = [1, 2, 3, 4, 6, 7, 8]

#produto = 1

#for n in numeros:
  #produto = produto * n

#print("O produto dos números é:", produto)

funcionarios = {
  "Alice": ["2", "0", "2", "5"],
  "Bob": ["4", "5", "3", "2"],
  "Charlie": ["1", "9", "9", "8"],
}

for nome, senha in funcionarios.items():
  senha_correta = "".join(senha)

print(f"{nome}: {senha_correta}")
