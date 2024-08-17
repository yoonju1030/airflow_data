import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="fruit_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 8, 5, 23, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["fruit", "test"],
) as dag:

    t1_orange = BashOperator(
        task_id="t1_orange",
        bash_command="/home/allrealjgt/airflow_data/plugins/select_fruit.sh ORANGE"
    )

    t2_avocado = BashOperator(
        task_id="t2_avocado",
        bash_command="/home/allrealjgt/airflow_data/plugins/select_fruit.sh AVOCADO"
    )

    # task 수행 순서
    t1_orange >> t2_avocado