import random
import string

def encrypt(nomes):
    # Gera uma chave aleatória entre 1 e 10
    chave_aleatoria = random.randint(1, 10)

    # Criptografa cada nome
    nomes_cript = []
    for nome in nomes:
        cript = ""
        for c in nome:
            if c.isalpha():
                if c.isupper():
                    cript += chr((ord(c) - 65 + chave_aleatoria) % 26 + 65)
                else:
                    cript += chr((ord(c) - 97 + chave_aleatoria) % 26 + 97)
            else:
                cript += c
        nomes_cript.append(cript)

    return nomes_cript, chave_aleatoria

nomes = ["Laura", "Flávia", "Philippe", "Gabriel", "Vitótia", "Luiz"]
nomes_cript, chave_aleatoria = encrypt(nomes)
print("Nomes criptografados:", nomes_cript)
print("Chave de criptografia:", chave_aleatoria)