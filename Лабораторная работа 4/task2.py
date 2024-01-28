import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as file_in:
        reader = [line for line in csv.DictReader(file_in)]
    with open(OUTPUT_FILENAME, 'w') as file_out:
        file_out.write(json.dumps(reader, indent=4))


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end='')
