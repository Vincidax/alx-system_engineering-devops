#!/usr/bin/python3
"""
Generate a Todo list for a given employee id
"""


import json
import requests
from sys import argv


def export_tasks_to_json(user_id):
    """
    Exports tasks for a given user ID to a JSON file
    """
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + f"users/{user_id}").json()
    todos = requests.get(url + f"todos", params={"userId": user_id}).json()

    tasks = [
        {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user.get("username")
        }
        for todo in todos
    ]

    data = {str(user_id): tasks}

    with open(f"{user_id}.json", "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    user_id = argv[1] if len(argv) > 1 else input("Enter User ID: ")
    export_tasks_to_json(user_id)
