# Solicita a frase do usuário
frase = input("Digite uma frase: ")

# Define as vogais a serem substituídas
vogais = 'aeiouAEIOU'

# Substitui as vogais por "*"
frase_modificada = ''.join('*' if char in vogais else char for char in frase)

# Imprime a frase modificada
print(f"Frase modificada: {frase_modificada}")


#Este programa solicita ao usuário inserir uma frase e define as vogais que devem ser substituídas por "". Em seguida, utiliza uma expressão geradora para substituir cada caractere da frase por "" se for uma vogal, ou por si mesmo se não for uma vogal. Por fim, imprime a frase modificada.