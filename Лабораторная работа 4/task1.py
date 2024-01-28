import json


FILENAME = "input.json"


def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)
    sum_multiplication = sum([i['score'] * i['weight'] for i in json_data])
    return round(sum_multiplication, 3)


print(task())
