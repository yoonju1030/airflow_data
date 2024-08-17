import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from common.common_func import select_shohoku

with DAG(
    dag_id="dags_python_import_func",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 8, 5, 23, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["python", "dags", "import"],
) as dag:

    py_t1 = PythonOperator(
        task_id="py_t1",
        python_callable=select_shohoku
    )

    py_t1 