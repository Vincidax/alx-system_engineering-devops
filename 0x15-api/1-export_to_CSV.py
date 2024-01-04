#!/usr/bin/python3
"""
Generate a Todo list for a given employee id and export it to CSV
"""
import csv
import requests
from sys import argv


def export_to_csv(employee_id):
    """
    Generates a CSV file with tasks for the given employee ID
    """
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + f"users/{employee_id}").json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    tasks = [
        (
            employee_id,
            user.get('username'),
            str(task.get("completed")),
            task.get("title")
        )
        for task in todos
    ]

    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"])
        csv_writer.writerows(tasks)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
    else:
        employee_id = argv[1]
        export_to_csv(employee_id)
