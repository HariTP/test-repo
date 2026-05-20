from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable, Connection
from airflow.hooks.base import BaseHook
from datetime import datetime

def print_api_key():
    try:
        import tqdm
    except Exception as e:
        print(e)
    try:
        import yfinance
    except Exception as e:
        print(e)
    # Fetch the variable
    api_key = Variable.get("news_api_key")
    if api_key=="hello_variable":
        print("success ho gya3")
    else:
        print("fail3")
    print(f"News API Key is: {api_key}")

default_args = {
    'start_date': datetime(2023, 1, 1),
}

with DAG(
    dag_id='dummy_variable_print_dag',
    default_args=default_args,
    schedule_interval=None,  # Manual run
    catchup=False,
    tags=['example'],
) as dag:

    task_print_var = PythonOperator(
        task_id='print_news_api_key',
        python_callable=print_api_key,
    )
