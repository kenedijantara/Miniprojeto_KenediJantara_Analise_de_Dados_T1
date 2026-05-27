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

# PASSO 2 - Carregamento da base com Pandas
print("\n[PASSO 2] Carregando os dados com Pandas...")

df = pd.read_csv(nome_arquivo, sep=';')

# Remover colunas totalmente vazias
df = df.dropna(how='all', axis=1)

print("\n--- Informações da Base ---")
print(f"Quantidade de linhas: {df.shape[0]}")
print(f"Quantidade de colunas: {df.shape[1]}")

print("\n--- Tipos de Dados ---")
print(df.dtypes)

print("\n--- Verificação de Problemas ---")
print("Valores nulos por coluna:")
print(df.isnull().sum())

print(f"\nQuantidade de linhas duplicadas: {df.duplicated().sum()}")

print("=" * 50)