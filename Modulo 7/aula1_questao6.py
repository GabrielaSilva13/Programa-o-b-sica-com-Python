from collections import Counter

def encontrar_anagramas(frase, palavra_objetivo):
    # Cria um dicionário com a contagem de caracteres da palavra objetivo
    contagem_objetivo = Counter(palavra_objetivo)

    anagramas = []

    # Percorre a frase em busca de anagramas
    for i in range(len(frase) - len(palavra_objetivo) + 1):
        palavra = frase[i:i+len(palavra_objetivo)]
        
        # Verifica se a palavra tem a mesma contagem de caracteres que a palavra objetivo
        if Counter(palavra) == contagem_objetivo:
            anagramas.append(palavra)

    return anagramas

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

anagramas = encontrar_anagramas(frase, palavra_objetivo)
print("Anagramas:", anagramas)