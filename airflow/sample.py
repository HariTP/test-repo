from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable, Connection
from airflow.hooks.base import BaseHook
from datetime import datetime

def print_api_key():
    # Fetch the variable
    api_key = Variable.get("news_api_key")
    api_key_local = Variable.get("news_api_key_local")
    api_key_secret = Variable.get("news_api_key_secret")
    api_key_secret_local = Variable.get("news_api_key_secret_local")
    if api_key_local=="hello_variable_local":
        print("success ho gya1")
    else:
        print("fail1")
    if api_key_secret=="hello":
        print("success ho gya2")
    else:
        print("fail2")
    if api_key=="hello_variable":
        print("success ho gya3")
    else:
        print("fail3")
    if api_key_secret_local=="hello_local":
        print("success ho gya4")
    else:
        print("fail4")
    print(f"News API Key is: {api_key}")
    print(f"News API Key secret is: {api_key_secret}")
    conn_id = 'my_conn'
    conn: Connection = BaseHook.get_connection(conn_id)
    
    # Assemble full DB URL
    db_url = conn.get_uri()
    print(f"Database connection URI = {db_url}")

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
