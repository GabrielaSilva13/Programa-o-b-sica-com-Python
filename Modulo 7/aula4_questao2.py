import os
import re

# Obtém o caminho absoluto do diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Cria o caminho completo do arquivo
frase_path = os.path.join(script_dir, "frase.txt")

# Verifica se o arquivo existe
if not os.path.exists(frase_path):
    print(f"Arquivo '{frase_path}' não encontrado.")
    exit()

# Abre o arquivo e lê o conteúdo
with open(frase_path, "r") as arquivo:
    conteudo = arquivo.read()

# Remove espaços em branco e caracteres não alfabéticos
palavras = re.sub(r'\W+', ' ', conteudo).split()

# Salva as palavras em um novo arquivo
palavras_path = os.path.join(script_dir, "palavras.txt")
with open(palavras_path, "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")

# Imprime o conteúdo do arquivo "palavras.txt"
print(f"Conteúdo do arquivo 'palavras.txt':")
with open(palavras_path, "r") as arquivo:
    print(arquivo.read())