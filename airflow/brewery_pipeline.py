from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import datetime as dt
import papermill as pm

def run_notebook(notebook_path, output_path):
    pm.execute_notebook(
        notebook_path,
        output_path
    )

default_args = {
    'owner': 'airflow'
    ,'trigger_rule':'all_success'
    ,'depends_on_past': False
    ,'execution_timeout':dt.timedelta(minutes=10)
    ,'retries': 2
    ,'retry_delay': dt.timedelta(minutes=5)
    ,'start_date': dt.datetime(2024, 7, 26)
}

with DAG(
    dag_id='brewery_pipeline'
    ,default_args=default_args
    ,schedule_interval='@daily'
    ,dagrun_timeout=dt.timedelta(minutes=30)
    ,description='Pipeline para tratar os dados de cervejarias da openbrewerydb.'
) as dag:
    load_bronze_breweries = PythonOperator(
        task_id='load_bronze_breweries',
        python_callable=run_notebook,
        op_kwargs={'notebook_path': '../notebooks/load_bronze_breweries.ipynb', 'output_path': '../notebooks/_temp/load_bronze_breweries.ipynb'},
    )

    load_silver_breweries = PythonOperator(
        task_id='load_silver_breweries',
        python_callable=run_notebook,
        op_kwargs={'notebook_path': '../notebooks/load_silver_breweries.ipynb', 'output_path': '../notebooks/_temp/load_silver_breweries.ipynb'},
    )

    load_gold_breweries = PythonOperator(
        task_id='load_gold_breweries',
        python_callable=run_notebook,
        op_kwargs={'notebook_path': '../notebooks/load_gold_breweries.ipynb', 'output_path': '../notebooks/_temp/load_gold_breweries.ipynb'},
    )

    load_bronze_breweries >> load_silver_breweries >> load_gold_breweries
