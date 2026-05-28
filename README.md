# Miniprojeto - Análise de Dados de Varejo

Projeto desenvolvido em Python utilizando Pandas para análise exploratória e limpeza de dados da base Varejo.csv.

## Autor

Kenedi Nazário Jantara

## Objetivo

Realizar uma análise exploratória dos dados, identificar problemas na base, aplicar tratamento de dados e gerar estatísticas descritivas.

## Funcionalidades Desenvolvidas

* Leitura do arquivo CSV
* Extração utilizando csv.DictReader
* Verificação de valores nulos
* Remoção de duplicatas
* Conversão de dados
* Estatísticas descritivas
* Agrupamentos com groupby()
* Exportação da base limpa

## Principais Insights

* A categoria ALIMENTOS apresentou o maior volume de vendas.
* O público feminino realizou mais compras na base analisada.
* Foram identificadas mais de 96 mil linhas duplicadas.
* A maioria dos clientes possui 0 filhos.
* A base apresentou boa qualidade por não possuir valores nulos nas principais colunas.

## Reflexão Teórica

O processo de ETL (Extração, Transformação e Carga) é fundamental para preparar dados para análise. Durante o projeto foi possível compreender a importância da limpeza dos dados, remoção de duplicatas e padronização dos tipos de dados para garantir análises mais confiáveis.

Além disso, a qualidade dos dados impacta diretamente nos resultados obtidos em análises e dashboards, tornando essencial a validação e tratamento das informações antes da utilização.

## Tecnologias Utilizadas

* Python
* Pandas
* CSV

## Estrutura do Projeto

* Base Varejo.csv → Base original utilizada na análise.
* Varejo_Limpo.csv → Arquivo gerado após o tratamento dos dados.
* analise_varejo.py → Script principal da análise exploratória.
* README.md → Documentação principal do projeto.
* README_KenediJantara_Analise_de_Dados_T1.md → Instruções para execução do projeto.