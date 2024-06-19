import os

# Solicita a frase do usuário
frase = input("Digite uma frase: ")

# Obtém o caminho absoluto do diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Cria o caminho completo do arquivo
arquivo_path = os.path.join(script_dir, "frase.txt")

# Salva a frase no arquivo
with open(arquivo_path, "w") as arquivo:
    arquivo.write(frase)

# Imprime o caminho completo do arquivo salvo
print(f"Frase salva em {arquivo_path}")


# Dessa forma, você pode facilmente localizar o arquivo "frase.txt" que contém a frase digitada pelo usuário.