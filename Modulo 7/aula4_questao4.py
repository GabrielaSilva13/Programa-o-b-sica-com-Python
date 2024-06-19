import random

# Abre o arquivo com as palavras
with open('gabarito_forca.txt', 'r') as file:
    gabarito = file.read().splitlines()

# Escolhe uma palavra aleatória
palavra_secreta = random.choice(gabarito)

# Abre o arquivo com os estágios do enforcado
with open('gabarito_enforcado.txt', 'r') as file:
    enforcado = file.read().splitlines()

# Inicializa a variável para armazenar a palavra com underscores
palavra_mostra = ['_'] * len(palavra_secreta)

# Inicializa a variável para armazenar o número de erros
erros = 0

# Loop principal do jogo
while True:
    # Mostra a palavra com underscores
    print(' '.join(palavra_mostra))

    # Pede ao jogador que insira uma letra
    letra = input('Insira uma letra: ').lower()

    # Verifica se a letra está na palavra
    if letra in palavra_secreta:
        # Substitui os underscores correspondentes à letra digitada
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                palavra_mostra[i] = letra
    else:
        # Incrementa o número de erros
        erros += 1

        # Imprime o enforcado correspondente
        print(enforcado[erros - 1])

    # Verifica se o jogador acertou a palavra
    if '_' not in palavra_mostra:
        print('Parabéns, você acertou a palavra!')
        break

    # Verifica se o jogador atingiu o número máximo de erros
    if erros == 6:
        print('Você foi enforcado!')
        break