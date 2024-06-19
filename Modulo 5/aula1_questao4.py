import datetime

# Obtém a data e hora atuais
now = datetime.datetime.now()

# Formata a data
data = now.strftime("%d/%m/%Y")

# Formata a hora
hora = now.strftime("%H:%M")

# Exibe a data e hora
print(f"Data: {data}")
print(f"Hora: {hora}")