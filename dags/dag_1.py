# Step 1 - Import modules

from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator

# Step 2 - Define default arguments

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 12, 6),
    'retries': 0
}
# Step 3 - Instantiate the DAG

dag = DAG(dag_id='DAG_1', default_args=default_args, catchup=False, schedule_interval='@once')

# Step 4 - Define tasks

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

# Step 5 - Define dependencies

start >> end

