# Solicita do usuário uma quantidade indefinida de números inteiros
numeros = []
while True:
    try:
        num = int(input("Insira um número inteiro (ou 's' para parar): "))
        if num == 's':
            break
        numeros.append(num)
    except ValueError:
        print("Por favor, insira um valor inteiro.")

# Imprime a lista original
print("Lista original:", numeros)

# Imprime os 3 primeiros elementos
print("3 primeiros elementos:", numeros[:3])

# Imprime os 2 últimos elementos
print("2 últimos elementos:", numeros[-2:])

# Imprime a lista invertida
print("Lista invertida:", numeros[::-1])

# Imprime os elementos de índice par
print("Elementos de índice par:", [numeros[i] for i in range(0, len(numeros), 2)])

# Imprime os elementos de índice ímpar
print("Elementos de índice ímpar:", [numeros[i] for i in range(1, len(numeros), 2)])