import random

# Gera 20 valores aleatórios entre -100 e 100
valores = [random.randint(-100, 100) for _ in range(20)]

# Impressão da lista ordenada
print("Lista ordenada:", sorted(valores))

# Impressão da lista original
print("Lista original:", valores)

# Encontra o índice do maior valor
max_valor = max(valores)
max_index = valores.index(max_valor)

# Encontra o índice do menor valor
min_valor = min(valores)
min_index = valores.index(min_valor)

# Impressão do índice do maior valor
print("Índice do maior valor:", max_index)

# Impressão do índice do menor valor
print("Índice do menor valor:", min_index)