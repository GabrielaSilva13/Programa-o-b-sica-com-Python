def validador_senha(senha):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False

    # Verifica se a senha contém pelo menos uma letra maiúscula
    if not any(char.isupper() for char in senha):
        return False

    # Verifica se a senha contém pelo menos uma letra minúscula
    if not any(char.islower() for char in senha):
        return False

    # Verifica se a senha contém pelo menos um número
    if not any(char.isdigit() for char in senha):
        return False

    # Verifica se a senha contém pelo menos um caractere especial
    if not any(not char.isalnum() for char in senha):
        return False

    # Se a senha atende a todos os critérios, retorna True
    return True

# Exemplo de uso:
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validador_senha(senha1))  # Saída esperada: True
print(validador_senha(senha2))  # Saída esperada: False
print(validador_senha(senha3))  # Saída esperada: False


# Essa função utiliza a biblioteca random para embaralhar as letras internas de cada palavra. Primeiramente, separa a frase em palavras. Em seguida, embaralha as letras internas de cada palavra, mantendo a primeira e a última letra no lugar correto. Por fim, junta as palavras embaralhadas em uma frase e retorna o resultado.