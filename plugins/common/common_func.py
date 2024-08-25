from airflow.decorators import task
import random
import requests
import os
import json

def select_shohoku():
    fruit = ["akagi", "miyagi", "sakuragi", "rukawa", "mitsui"]
    rand_int = random.randint(0, len(fruit)-1)
    print(fruit[rand_int])

@task(task_id="python_task_01")
def print_context(some_input):
    print(some_input)

@task(task_id="laftel_test")
def get_info_anime():
    url = os.environ["LAFTEL_URL"].format(query="슬램덩크")
    headers={
        "laftel": os.environ["LAFTEL_VALUE"],
        "User-Agent": os.environ["USER_AGENT"]
    }
    resp_raw = requests.get(url=url, headers=headers)
    resp = json.loads(resp_raw.text)
    print(resp['results'][0]["img"])