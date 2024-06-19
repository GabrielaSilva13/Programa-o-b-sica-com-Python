import os

# Verifica se o arquivo existe
if not os.path.exists("estomago.txt"):
    print("Arquivo 'estomago.txt' não encontrado.")
    exit()

# Abre o arquivo para leitura
with open("estomago.txt", "r") as arquivo:
    conteudo = arquivo.readlines()

# Imprime as primeiras 25 linhas
print("Primeiras 25 linhas:")
for linha in conteudo[:25]:
    print(linha.strip())

# Imprime o número de linhas do arquivo
print(f"Total de linhas: {len(conteudo)}")

# Encontra a linha com maior número de caracteres
max_caracteres = max(len(linha.strip()) for linha in conteudo)
max_linha = [linha for linha in conteudo if len(linha.strip()) == max_caracteres][0]
print(f"Linha com maior número de caracteres: {max_linha.strip()}")

# Encontra o número de menções aos nomes dos personagens "Nonato" e "Íria"
nonato_count = sum(1 for linha in conteudo if "nonato" in linha.lower())
íria_count = sum(1 for linha in conteudo if "íria" in linha.lower())
print(f"Menções a 'Nonato': {nonato_count}")
print(f"Menções a 'Íria': {íria_count}")


# baixe o arquivo 