import csv
import os
from datetime import datetime
from rich import print


def log_to_csv(problemID, start_time, end_time, duration, solved, difficulty, tags, notes):
    file_name = datetime.now().strftime("%Y-%m-%d")
    file_to_find= f"log/{file_name}.csv"
    header_row = ['Problem ID', 'Start Time', 'End Time', 'Duration', 'Solved', 'Difficulty', 'Tags', 'Notes']
    data_row = [problemID, start_time, end_time, duration, solved, difficulty, tags, notes]

    if not os.path.exists(file_to_find):
        if not os.path.exists('log'):
            os.makedirs('log', exist_ok=True)
        with open(file_to_find, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header_row)
        print(f"[blue]CSV file {file_name} created successfully[/blue]")

    with open(file_to_find, 'a', newline='') as file:
        writer= csv.writer(file)
        writer.writerow(data_row)
    print(f"[blue]Data for the Problem ID {problemID} successfully logged[/blue]")

