# Step 1 - Import modules
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from clean_data import import_raw_data

# Step 2 - Define default arguments

default_args = {
    'owner': 'airflow',
    'retry_delay': timedelta(minutes=5),
    'retries': 1,
    'depends_on_past': False
}

with DAG(dag_id="overdose_dag",
         start_date=datetime(2021, 1, 1),
         schedule_interval="@once",
         catchup=False,
         default_args=default_args) as dag:

    task_I = PythonOperator(
        task_id="overdose_process",
        python_callable=import_raw_data,
        dag=dag
    )

