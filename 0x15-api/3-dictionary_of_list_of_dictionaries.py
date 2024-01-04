#!/usr/bin/python3
"""
Generate a Todo list for all employees
"""


import json
import requests


def export_all_tasks_to_json():
    """
    Exports tasks for all users to a JSON file
    """
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()

    all_tasks = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        todos = requests.get(url + f"/{user_id}/todos").json()

        tasks = [
            {
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            for todo in todos
        ]

        all_tasks[str(user_id)] = tasks

    with open("todo_all_employees.json", "w") as file:
        json.dump(all_tasks, file)


if __name__ == "__main__":
    export_all_tasks_to_json()
