import random

# Gera um valor aleatório entre 5 e 20
num_elementos = random.randint(5, 20)

# Gera valores aleatórios entre 1 e 10 em quantidade correspondente a num_elementos
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Impressão da lista elementos
print("Lista elementos:", elementos)

# Impressão da soma dos valores da lista
print("Soma dos valores da lista:", sum(elementos))

# Impressão da média dos valores da lista
print("Média dos valores da lista:", sum(elementos) / num_elementos)