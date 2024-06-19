import csv
import pandas as pd

with open('spotify-2023.csv', 'r', encoding='latin-1') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)

dados = list(leitor)    

dados_filtrados = [linha for linha in dados if 2012 <= int(linha[3]) <= 2022]

dados_processados = []
for linha in dados_filtrados:
    if '"' in linha[1]:
        continue
    dados_processados.append([linha[0], linha[1], int(linha[3]), int(linha[7])])

dados_organizados = {}
for linha in dados_processados:
    if linha[2] not in dados_organizados:
        dados_organizados[linha[2]] = []
    dados_organizados[linha[2]].append(linha)    

lista_produzida = []
for ano, linhas in dados_organizados.items():
    linhas.sort(key=lambda x: x[3], reverse=True)
    lista_produzida.extend(linhas[:10])    

print(lista_produzida)

import csv
import pandas as pd

with open('spotify-2023.csv', 'r', encoding='latin-1') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)

dados = list(leitor)

dados_filtrados = [linha for linha in dados if 2012 <= int(linha[3]) <= 2022]

dados_processados = []
for linha in dados_filtrados:
    if '"' in linha[1]:
        continue
    dados_processados.append([linha[0], linha[1], int(linha[3]), int(linha[7])])

dados_organizados = {}
for linha in dados_processados:
    if linha[2] not in dados_organizados:
        dados_organizados[linha[2]] = []
    dados_organizados[linha[2]].append(linha)

lista_produzida = []
for ano, linhas in dados_organizados.items():
    linhas.sort(key=lambda x: x[3], reverse=True)
    lista_produzida.extend(linhas[:10])

print(lista_produzida)