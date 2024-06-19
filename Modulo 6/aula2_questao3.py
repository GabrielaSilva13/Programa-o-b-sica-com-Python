import random

# Gera 20 valores aleatórios entre 0 e 50 para lista1
lista1 = [random.randint(0, 50) for _ in range(20)]

# Gera 20 valores aleatórios entre 0 e 50 para lista2
lista2 = [random.randint(0, 50) for _ in range(20)]

# Cria a lista intersecção com os valores que se repetem nas duas listas
interseccao = list(set([i for i in lista1 if i in lista2]))

# Impressão das listas
print("Lista1:", lista1)
print("Lista2:", lista2)

# Impressão da lista intersecção ordenada
print("Interseccao:", sorted(interseccao))

# Contagem de cada elemento em cada lista
contagem = {}
for elemento in lista1:
    if elemento in contagem:
        contagem[elemento] += 1
    else:
        contagem[elemento] = 1

for elemento in lista2:
    if elemento in contagem:
        contagem[elemento] += 1
    else:
        contagem[elemento] = 1

# Impressão da contagem
for elemento, contagem_elemento in contagem.items():
    print(f"{elemento}: (lista1={contagem_elemento}, lista2={contagem_elemento})")