N = int(input("Digite a quantidade de respondentes: "))
total_idades = 0
contador = 0
while contador < N:
    idade = int(input(f"Digite a idade do respondente {contador + 1}: "))
    total_idades += idade
    contador += 1

    print(f"A média das idades dos respondentes é de: {total_idades / N:.0f} anos")
