

idade = int(input("Digite sua idade: "))
jogou_tres_jogos = input("Você já jogou pelo menos 3 jogos de tabuleiro? (True/False) ")
jogou_tres_jogos = jogou_tres_jogos.lower() == 'true'  # Converte para booleano
vezes_venceu = int(input("Quantos jogos já venceu? "))

if 16 <= idade <= 18 and jogou_tres_jogos and vezes_venceu >= 1:
        print(True)
        print("Parabéns! Bem vindo ao clube juvenil de jogos de tabuleiro.")
else:
        print(False)
        print("Você não cumpre os requisitos para ingressar no clube .")

