# 2015 -> Relatório IDC patrocinado pela Seagate -> International Data Corporation, no ano de 2015 eles informaram que cada pessoa na terra que possuia acesso a internet, seja por redes sociais, mecanismos de pesquisa, interações na web, ligações via internet...produzia 1,3 GB de dados por dia.

# Arrays -> São estruturas que conseguem guardar uma quantidade imensa de informação, porém de forma desorganizada. --> Em Pytho chamamos de Listas, em algumas líguagens podem ser Vetor ou Matriz.

lista_dos_sonhos = ["Viajar mais", "estabilizar a vida", "bem empregado"]

print(lista_dos_sonhos)
print(type(lista_dos_sonhos))
print(type(lista_dos_sonhos[0]))

# Indexação Negativa

print(lista_dos_sonhos[-1])

# Métodos de Listas

# insert -> Adiciona uma informação na lista em um local específico que quisermos.

lista_dos_sonhos.insert(0, "Pagar o que deve")

print(lista_dos_sonhos)

# Append -> Adiciona uma informação ao final da nossa lista

lista_dos_sonhos.append("Viajar o mundo")

print(lista_dos_sonhos)

# sort -> Ordena as informações da nossa lista em formato alfanúmerido, alfabética, crescente e descrecente

nomes = ["Plínio", "Camila", "Júlia", "Alisson", "Luis Otávio"]

nomes.sort()
#nomes.sort(reverse=True)

print(nomes)

# remove -> Retira a informação que definimos na lista

nomes.remove("Plínio")
print(nomes)

# pop -> Retira a informação baseado no  índice que colocarmos

nomes.pop(0)
print(nomes)

# index() -> Vai retornar o índice do valor pesquisado