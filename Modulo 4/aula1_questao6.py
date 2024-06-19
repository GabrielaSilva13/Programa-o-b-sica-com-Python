
N = int(input("Digite a quantidade de experimentos registrados: "))
total_cobaias = 0
contagem_sapos,contagem_ratos,contagem_coelhos = 0,0,0
contador = 0

while contador < N:
    quantia, tipo = input("Digite a quantidade e o tipo de cobaia (S: Sapo, R: Rato, C: Coelho), separados por espaço: ").split()
    quantia = int(quantia)
            
    if tipo == 'S':
     contagem_sapos += quantia
    elif tipo == 'R':
     contagem_ratos += quantia
    elif tipo == 'C':
     contagem_coelhos += quantia

    total_cobaias += quantia
    contador += 1

    print("\nResultados:")
    print(f"Total de cobaias utilizadas: {total_cobaias}")
    print(f"Total de sapos: {contagem_sapos} ({(contagem_sapos / total_cobaias) * 100:.2f}%)")
    print(f"Total de ratos: {contagem_ratos} ({(contagem_ratos / total_cobaias) * 100:.2f}%)")
    print(f"Total de coelhos: {contagem_coelhos} ({(contagem_coelhos / total_cobaias) * 100:.2f}%)")

 