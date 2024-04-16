#!/usr/bin/python3
"""
Script that uses a REST API to return informations
about an employee's progress.
"""

import requests
from sys import argv
import json


if __name__ == "__main__":

    infos = requests.get(
        "https://jsonplaceholder.typicode.com/users")
    employees = infos.json()

    data = {}
    for employee in employees:
        emp_id = employee.get("id")
        infos = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id))
        todos = infos.json()
        data[emp_id] = [{"task": task.get("title"),
                         "completed": task.get("completed"),
                         "username": employee.get("username")}
                        for task in todos]

    with open("todo_all_employees.json", "w") as json_f:
        json_f.write(json.dumps(data))
