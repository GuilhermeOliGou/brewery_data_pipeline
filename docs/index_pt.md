# BREWERY DATA PIPELINE

## Objetivos

Brewery é um projeto de data engineering, com o objetivo de praticar e exercitar tópicos tais como: uso de tecnologias de processamento de dados; integração com ferramentas de data quality e code quality; modelagem de dados e construção de pipelines, e; aplicação das boas práticas para projetos de dado.

## Estrutura do Datalake

O projeto implementa um pipeline que processas dados em batch e gera um datalake de arquivos locais com uma estrutura medalhão, com cada camada sendo prganizada hierarquicamente por Data Source, Data Context e Data Entity:

1. **Camada Bronze**: Armazenamento de dados crús da forma como são ingeridos das fontes.
2. **Camada Prata**: Transformação e armazenamento de dados formatados próprios para consultas e análises.
3. **Camada Ouro**: Dados agregados em visualizações para análises de negócio e consumo por modelos de machine learning.

## Ferramentas e Tecnologias

- **Fontes de Dados**: [Open Brewery DB API](https://api.openbrewerydb.org/breweries)
- **Orquestrador**: Apache Airflow
- **Processamento de Dados**: Python com PySpark, Delta Spark e Jupyter notebooks
- **CI/CD**: Git hub actions com a biblioteca Unittest de Python
- **Qualidade de Dados**: Biblioteca Great Expectations
- **Conteinerização**: Docker

## Transformações de Dado

O projeto faz manipulações estáticas em um conjunto de dados público e as transformações foram desenhadas da seguinte forma:

1. **Camada Bronze**: Os dados de cervejarias são ingeridos da fonte pública [Open Brewery DB API](https://api.openbrewerydb.org/breweries) e armazenados sem alteração usando arquivos JSON.
2. **Camada Prata**: Os dados são deduplicados, formatados e armazenados em tabelas delta particionadas por localidade.
3. **Camada Ouro**: Os dados são agregados em uma visão que sumariza a quantidade de cervejarias por tipo e localidade.

## Repository Structure

brewery_data_pipeline/
│
├── airflow/
│   └── dag_1.py
│
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── requirements.txt
│
├── docs/
│   └── docs_1.md
│
├── gx/
│   ├── expectations/
│   │   └── expectations.json
│   └── expectations_generator.py
│
├── notebooks/
│   ├── data_transformation_notebook_1.ipynb
│   ├── data_transformation_notebook_2.ipynb
│   └── data_transformation_notebook_3.ipynb
│
├── src/
│   └── utils.py
│
├── tests/
│   └── test_src.py
│
├── LICENSE
│
└── README.md

## Roadmap

### Até 17 de agosto
- [x] Notebooks de transformação
- [x] DAG do Airflow
- [x] Criação da biblioteca local src

### Até 24 de agosto
- [x] Validações do great expectations

### Até 01 de julho de 2025
- [ ] Testes unitários
- [ ] CI/CD com o Github actions
- [ ] Conteineirização usando Docker

### Atualizações
- **2024-07-19**: Início do projeto
- **2024-07-26**: Lançamento da feature Notebooks de transformação
- **2024-07-26**: Lançamento da feature DAG do Airflow
- **2024-07-26**: Lançamento da feature Criação da biblioteca local src
- **2024-08-13**: Atualização do roadmap
- **2024-08-20**: Repriorização de features
- **2024-08-24**: Lançamento da feature Validações do great expectations
- **2024-09-09**: Atualização do roadmap