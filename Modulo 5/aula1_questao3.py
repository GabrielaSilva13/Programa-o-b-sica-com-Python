import random

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

while True:
    # Peça ao usuário para adivinhar o número
    palpite = int(input("Adivinhe o número entre 1 e 10: "))

    # Verifica se o palpite é correto
    if palpite == numero_secreto:
        print(f"Parabéns Você acertou: {numero_secreto}")
        break

    # Verifica se o palpite é muito alto
    elif palpite > numero_secreto:
        print("O seu palpite é muito alto. Tente novamente!")

    # Verifica se o palpite é muito baixo
    else:
        print("O seu palpite é muito baixo. Tente novamente!")