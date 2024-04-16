#!/usr/bin/python3
"""
Script that uses a REST API to return informations
about an employee's progress. 
"""

import requests
from sys import argv


if __name__ == "__main__":

    user_id = argv[1]

    infos = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    user = infos.json()
    EMPLOYEE_NAME = user.get("name")

    infos = requests.get('https://jsonplaceholder.typicode.com/todos?userID={}'.format(user_id))
    todos = infos.json()
    TOTAL_NUMBER_OF_TASKS = len(todos)

    NUMBER_OF_DONE_TASKS = [task for task in todos if task.get("completed") is True]

    print("Employee {} is done with task({}/{}):".format
          (EMPLOYEE_NAME, len(NUMBER_OF_DONE_TASKS), TOTAL_NUMBER_OF_TASKS))

    for task in NUMBER_OF_DONE_TASKS:
        title = task.get("title")
        print("\t {}".format(title))
