import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
import random

with DAG(
    dag_id="dags_python_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 8, 5, 23, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["python", "dags"],
) as dag:
    def select_shohoku():
        fruit = ["akagi", "miyagi", "sakuragi", "rukawa", "mitsui"]
        rand_int = random.randint(0, len(fruit)-1)
        print(fruit[rand_int])
    py_t1 = PythonOperator(
        task_id="py_t1",
        python_callable=select_shohoku
    )

    py_t1 