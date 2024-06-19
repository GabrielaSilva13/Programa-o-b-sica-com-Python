# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Define as vogais
vogais = 'aeiouAEIOU'

# Cria a lista de vogais da frase
vogais_frase = [char for char in frase if char in vogais]

# Cria a lista de consoantes da frase
consoantes_frase = [char for char in frase if char not in vogais]

# Imprime a lista de vogais ordenada alfabeticamente
print("Vogais:", sorted(vogais_frase))

# Imprime a lista de consoantes
print("Consoantes:", consoantes_frase)