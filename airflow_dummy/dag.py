from datetime import datetime
import time

from airflow import DAG
from airflow.operators.python import PythonOperator


def sleep_and_print():
    print("Task started")
    print(">>> LATEST VERSION: force-sync fallback test <<<")

    time.sleep(60)

    print("Task completed after 60 seconds")


with DAG(
    dag_id="sample_sleep_dag",
    start_date=datetime(2026, 5, 6),
    schedule=None,  # Trigger manually
    catchup=False,
    tags=["example"],
) as dag:

    sleep_task = PythonOperator(
        task_id="sleep_and_print",
        python_callable=sleep_and_print,
    )