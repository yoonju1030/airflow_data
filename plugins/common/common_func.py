from airflow.decorators import task
import random

def select_shohoku():
    fruit = ["akagi", "miyagi", "sakuragi", "rukawa", "mitsui"]
    rand_int = random.randint(0, len(fruit)-1)
    print(fruit[rand_int])

@task(task_id="python_task_01")
def print_context(some_input):
    print(some_input)