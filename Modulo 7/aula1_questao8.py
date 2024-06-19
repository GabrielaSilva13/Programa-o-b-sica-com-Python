def validar_cpf(cpf):
    # Remover os pontos e o traço do CPF
    cpf = cpf.replace(".", "").replace("-", "")

    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return "Inválido"

    # Calcular o primeiro dígito verificador
    digitos = [int(d) for d in cpf[:9]]
    multiplicador = [x for x in range(10, 1, -1)]
    soma = sum([d * m for d, m in zip(digitos, multiplicador)])
    resto = soma % 11
    primeiro_digito = 0 if resto < 2 else 11 - resto

    # Calcular o segundo dígito verificador
    digitos = [int(d) for d in cpf[:10]]
    multiplicador = [x for x in range(11, 1, -1)]
    soma = sum([d * m for d, m in zip(digitos, multiplicador)])
    resto = soma % 11
    segundo_digito = 0 if resto < 2 else 11 - resto

    # Verificar se os dígitos verificadores estão corretos
    if int(cpf[-2]) == primeiro_digito and int(cpf[-1]) == segundo_digito:
        return "Válido"
    else:
        return "Inválido"

# Solicitar o CPF do usuário
cpf = input("Digite o CPF (no formato XXX.XXX.XXX-XX): ")

# Validar o CPF
resultado = validar_cpf(cpf)
print(resultado)