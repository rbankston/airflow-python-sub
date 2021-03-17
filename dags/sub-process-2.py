from airflow.models import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess
import shlex

default_args = {
 'start_date': datetime(2021, 1, 1)
}

def _sub_process():
    cmd = "python /usr/local/airflow/easy.py"
    ret = subprocess.run(shlex.split(cmd)).returncode
    if ret == 0:
        print("Task Completed With Success")
    else:
        print("Error")

with DAG('sub_processing', 
    schedule_interval='@hourly', 
    default_args=default_args,
    catchup=False) as dag:
    #Define tasks/operators

    sub = PythonOperator(
        task_id='sub',
        python_callable=_sub_process
    )



