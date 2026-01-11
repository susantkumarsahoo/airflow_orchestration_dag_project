from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

# Function executed by task
def say_hello():
    print("Hello World from Airflow!")

# DAG definition
with DAG(
    dag_id="hello_world_dag",
    start_date=datetime(2024, 1, 1),
    schedule=timedelta(minutes=5),  # Changed from schedule_interval to schedule
    catchup=False,
    max_active_runs=1
) as dag:
    hello_task = PythonOperator(
        task_id="hello_task",
        python_callable=say_hello
    )

# Run the DAG
# python airflow.dag.py














