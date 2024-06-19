# A: Para mulheres, ter mais de 60 anos. Para homens, 65 anos.
# B: Ou ter trabalhado pelo menos 30 anos.
# C: Ou ter 60 anos e trabalhado pelo menos 25 anos.


genero = input("Qual é o seu gênero? (M/F): ")
idade = int(input("Qual é a sua idade? "))
tempo = int(input("Quantos anos você trabalhou? "))

a = (genero == "F" and idade >= 60) or (genero =="M" and idade >=65)
b= tempo > 30
c = idade >=60 and tempo>=25
pode_aposentar = a or b or c

print(pode_aposentar)