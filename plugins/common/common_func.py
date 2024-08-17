from airflow.decorators import task
import random
import laftel

def select_shohoku():
    fruit = ["akagi", "miyagi", "sakuragi", "rukawa", "mitsui"]
    rand_int = random.randint(0, len(fruit)-1)
    print(fruit[rand_int])

@task(task_id="python_task_01")
def print_context(some_input):
    print(some_input)

@task(task_id="laftel_test")
def get_info_anime():
    laftel.sync.getAnimeInfo(query="슬램덩크")