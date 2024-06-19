# Recebe a quantidade de elementos da lista 1
n1 = int(input("Digite a quantidade de elementos da lista 1: "))

# Recebe os elementos da lista 1
lista1 = [int(input(f"Digite o {i+1}º elemento da lista 1: ")) for i in range(n1)]

# Recebe a quantidade de elementos da lista 2
n2 = int(input("Digite a quantidade de elementos da lista 2: "))

# Recebe os elementos da lista 2
lista2 = [int(input(f"Digite o {i+1}º elemento da lista 2: ")) for i in range(n2)]

# Combina as listas de forma alternada
lista_intercalada = []
for i in range(min(n1, n2)):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

# Adiciona os elementos remanescentes da maior lista
if n1 > n2:
    lista_intercalada.extend(lista1[n2:])
elif n2 > n1:
    lista_intercalada.extend(lista2[n1:])

# Impressão da lista intercalada
print("Lista intercalada:", lista_intercalada)