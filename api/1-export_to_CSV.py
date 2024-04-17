#!/usr/bin/python3
"""
Script that uses a REST API to return informations
about an employee's progress.
"""

import requests
from sys import argv
import csv


if __name__ == "__main__":

    user_id = argv[1]

    infos = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id))
    user = infos.json()
    employee = user.get("username")

    infos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id))
    todos = infos.json()

    with open("{}.csv".format(user_id), 'w') as csv_f:
        writer = csv.writer(csv_f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, employee,
                            task.get("completed"), task.get("title")])
