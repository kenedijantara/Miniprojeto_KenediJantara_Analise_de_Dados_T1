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

# PASSO 3 - Limpeza dos dados
print("\n[PASSO 3] Limpando os dados...")

# Remove linhas duplicadas
df = df.drop_duplicates()

print(f"Novo total de linhas após remoção: {df.shape[0]}")

# Conversão da coluna DATA
if 'DATA' in df.columns:

    df['DATA'] = pd.to_datetime(
        df['DATA'],
        format='%d/%m/%Y',
        errors='coerce'
    )

    print("Coluna DATA convertida com sucesso.")

# Tratamento da coluna PR_CAT
if 'PR_CAT' in df.columns:

    df['PR_CAT'] = df['PR_CAT'].fillna('Sem Categoria')

    df.loc[df['PR_CAT'] == '', 'PR_CAT'] = 'Sem Categoria'

    print("Tratamento da coluna PR_CAT realizado.")

else:
    print("Coluna PR_CAT não encontrada.")

# Tratamento da coluna DIMENSOES
if 'DIMENSOES' in df.columns:

    df['DIMENSOES'] = df['DIMENSOES'].fillna('0x0x0')

    print("Tratamento da coluna DIMENSOES realizado.")

else:
    print("A coluna DIMENSOES não foi encontrada na base.")

print("\n--- Tipos de Dados Após Conversão ---")
print(df.dtypes)

print("=" * 50)

# PASSO 4 - Estatísticas descritivas
print("\n[PASSO 4] Estatísticas Descritivas")

if 'CL_FHL' in df.columns:

    media = df['CL_FHL'].mean()
    mediana = df['CL_FHL'].median()
    desvio_padrao = df['CL_FHL'].std()
    moda = df['CL_FHL'].mode()[0]
    maximo = df['CL_FHL'].max()
    minimo = df['CL_FHL'].min()
    contagem = df['CL_FHL'].count()

    quartis = df['CL_FHL'].quantile([0.25, 0.50, 0.75])

    print(f"Média: {media:.2f}")
    print(f"Mediana: {mediana}")
    print(f"Desvio Padrão: {desvio_padrao:.2f}")
    print(f"Moda: {moda}")
    print(f"Máximo: {maximo}")
    print(f"Mínimo: {minimo}")
    print(f"Contagem: {contagem}")

    print("\nQuartis:")
    print(quartis)

else:
    print("Coluna CL_FHL não encontrada.")

print("=" * 50)

# PASSO 5 - Agrupamentos
print("\n[PASSO 5] Agrupamentos")

# Agrupamento por categoria
if 'PR_CAT' in df.columns and 'CO_ID' in df.columns:

    compras_por_categoria = (
        df.groupby('PR_CAT')['CO_ID']
        .count()
        .sort_values(ascending=False)
    )

    print("\nTop 5 categorias com mais vendas:")
    print(compras_por_categoria.head(5))

# Agrupamento por gênero
if 'CL_GENERO' in df.columns and 'CO_ID' in df.columns:

    compras_por_genero = (
        df.groupby('CL_GENERO')['CO_ID']
        .count()
        .sort_values(ascending=False)
    )

    print("\nQuantidade de compras por gênero:")
    print(compras_por_genero)

print("=" * 50)