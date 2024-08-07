# BREWERY DATA PIPELINE

## Objective

The Brewery is a practice project for data engineering, aiming to exercise topics such as: use of data processing technologies; integration with data quality and code quality tools; data modelling and pipeline building, and; application of the best practices for data projects.

## Datalake Structure

The project implements a pipeline that processes data in batches and generates a local file data lake with a medallion architecture, with each layer being organized hierarchically by Data Source, Data Context and Data Entity:

1. **Bronze Layer**: Storage of raw data as ingested from the sources.
2. **Silver Layer**: Transformation and storage of formatted data proper for querying and analysis.
3. **Gold Layer**: Data aggregated in views for business insights and consumption by machine learning models.

## Tools and Technologies

- **Data source**: [Open Brewery DB API](https://api.openbrewerydb.org/breweries)
- **Orchestration Tool**: Apache Airflow
- **Data Processing**: Python with PySpark, Delta Spark and Jupyter notebooks
- **CI/CD**: Git hub actions with Python Unittest library
- **Data Quality**: Great Expectations library
- **Containerization**: Docker

## Data Transformations

The project makes static manipulations of public data and the transformations were designed as follow:

1. **Bronze Layer**: The brewery data is ingested from the public source [Open Brewery DB API](https://api.openbrewerydb.org/breweries) and stored as-is using JSON files.
2. **Silver Layer**: The data is deduplicated, formatted and stored in delta tables partitioned by location.
3. **Gold Layer**: The data is aggregated in a view that summarizes the number of breweries by type and location.

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
├── great_expectations/
│   └── brewery_expectations.py
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

### Until August 12th
- [x] Transformation notebooks
- [x] Airflow DAG
- [x] Local library src
- [ ] Containerization using Docker

### Until August 16th
- [ ] Great Expectations validations

### Until August 23th
- [ ] Unit tests
- [ ] CI/CD with Github actions

### Updates
- **2024-07-19**: Project start
- **2024-07-26**: Release of the Transformation notebooks feature
- **2024-07-26**: Release of the Airflow DAG feature
- **2024-07-26**: Release of the Local library src feature