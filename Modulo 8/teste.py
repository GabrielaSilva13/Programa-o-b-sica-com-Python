def resultado_votacao(votos):
    total_votos = sum(sum(votos[i].values()) for i in range(len(votos)))
    resultado = {}
    for i in range(len(votos)):
        for candidato, votos_candidato in votos[i].items():
            if candidato not in resultado:
                resultado[candidato] = (0, 0)
            resultado[candidato] = (resultado[candidato][0] + votos_candidato, 
                                   (resultado[candidato][0] + votos_candidato) / total_votos * 100)
    return resultado

votos = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
]
resultado = resultado_votacao(votos)
print(resultado)
# Saída esperada: {'candidato_A': (360, 40.31), 'candidato_B': (258, 28.89), 'candidato_C': (275, 30.79)}