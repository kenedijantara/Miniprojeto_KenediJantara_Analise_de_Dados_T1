import csv
import pandas as pd

print("=" * 50)
print("INÍCIO DA ANÁLISE DE DADOS - VAREJO")
print("=" * 50)

nome_arquivo = 'Base Varejo.csv'

# PASSO 1 - Leitura inicial do arquivo CSV
print("\n[PASSO 1] Leitura inicial do arquivo CSV:")

with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:

    leitor = csv.DictReader(arquivo, delimiter=';')

    for indice, linha in enumerate(leitor):

        if indice < 2:
            print(f"Registro {indice + 1}: {linha}")

        else:
            break