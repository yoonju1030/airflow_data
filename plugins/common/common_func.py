import random

def select_shohoku():
    fruit = ["akagi", "miyagi", "sakuragi", "rukawa", "mitsui"]
    rand_int = random.randint(0, len(fruit)-1)
    print(fruit[rand_int])