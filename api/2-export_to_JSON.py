#!/usr/bin/python3
"""
Script that uses a REST API to return informations
about an employee's progress.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    user_id = argv[1]

    infos = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id))
    user = infos.json()
    employee = user.get("username")

    infos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id))
    todos = infos.json()

    tasks = []
    for todo in todos:
        task = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": employee
        }
        tasks.append(task)

    data = {user_id: tasks}
    with open("{}.json".format(user_id), "w") as js_f:
        js_f.write(json.dumps(data))
