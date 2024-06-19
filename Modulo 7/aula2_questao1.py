# Dicionário para mapear os números de meses para seus nomes por extenso
meses = {
    "01": "Janeiro",
    "02": "Fevereiro",
    "03": "Março",
    "04": "Abril",
    "05": "Maio",
    "06": "Junho",
    "07": "Julho",
    "08": "Agosto",
    "09": "Setembro",
    "10": "Outubro",
    "11": "Novembro",
    "12": "Dezembro"
}

# Solicita a data de nascimento do usuário
data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")

# Separa a data em dia, mês e ano
dia, mes, ano = map(int, data_nascimento.split('/'))

# Imprime a data com o nome do mês por extenso
print(f"Você nasceu em {dia} de {meses[str(mes)]} de {ano}")


#Este programa utiliza um dicionário para mapear os números de meses para seus nomes por extenso. Em seguida, solicita a data de nascimento do usuário e separa a data em dia, mês e ano. Por fim, imprime a data com o nome do mês por extenso.
