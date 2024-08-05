import datetime
import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

# DAG 정의 파트
# dag_id: DAG의 이름 (Python 파일명과는 상관 없지만 파일명과 아이디는 일치시키는 것이 좋다)
# schedule: cron 스케줄, 이 dag이 언제도는지
# start_date: 이 DAG이 언제부터 돌지, utc -> 9시간 늦게 돔
# catchup: False, True일 경우 batch로 한꺼번에 돌게 됨
# tags
# dagrun_timeout: pecify how long a DagRun should be up before timing out
with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 8, 5, 22, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["air", "flow"],
) as dag:
    # Task
    # bash_command: 어떤 쉘 스크립트를 출력할건지
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo 弱いジヌ"
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME"
    )

    # task 수행 순서
    bash_t1 >> bash_t2