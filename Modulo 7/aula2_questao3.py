while True:
    # Solicita a frase do usuário
    frase = input("Digite uma frase (digite 'fim' para encerrar): ")
    
    # Verifica se o usuário digitou "fim" para encerrar o programa
    if frase.lower() == "fim":
        break
    
    # Remove espaços em branco e sinais de pontuação da frase
    frase_limpa = ''.join(char for char in frase.lower() if char.isalnum())
    
    # Verifica se a frase é um palíndromo
    if frase_limpa == frase_limpa[::-1]:
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')

# Este programa utiliza um loop while para solicitar a frase do usuário até que ele digite "fim" para encerrar o programa. Dentro do loop, o programa remove os espaços em branco e sinais de pontuação da frase e a converte para minúsculas. Em seguida, verifica se a frase é um palíndromo comparando a frase limpa com sua versão invertida. Se a frase for um palíndromo, o programa imprime uma mensagem informando que a frase é um palíndromo. Caso contrário, imprime uma mensagem informando que a frase não é um palíndromo.        