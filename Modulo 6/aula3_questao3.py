import random

# Gera uma lista com 20 elementos entre -10 e 10
original = [random.randint(-10, 10) for _ in range(20)]
print("Original:", original)

# Encontra o intervalo que possui a maior quantidade de números negativos
negativos = [i for i, num in enumerate(original) if num < 0]
intervalo = (min(negativos), max(negativos))

# Deleta o intervalo da lista
del original[intervalo[0]:intervalo[1]+1]
print("Editada:", original)