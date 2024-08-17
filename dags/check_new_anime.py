import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from common.common_func import get_info_anime

with DAG(
    dag_id = "check_new_anime",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 8, 5, 23, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["fruit", "test"] 
) as dag:
    laftel_test = get_info_anime()
