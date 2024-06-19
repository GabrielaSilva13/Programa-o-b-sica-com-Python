frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
indices_vogais = []

for i, letra in enumerate(frase):
    if letra in vogais:
        indices_vogais.append(i)

num_vogais = len(indices_vogais)

print(f"{num_vogais} vogais")
print("Índices", indices_vogais)