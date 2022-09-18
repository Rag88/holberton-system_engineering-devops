#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    usrId = int(argv[1])
    todo_api_url = "https://jsonplaceholder.typicode.com/todos"
    todo_response = requests.get(todo_api_url).json()
    user_api_url = "https://jsonplaceholder.typicode.com/users/{}".\
        format(usrId)
    user_response = requests.get(user_api_url).json()
    EMPLOYEE_NAME = user_response.get("name")
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE_LIST = []
    for todo in todo_response:
        if todo.get("userId") == usrId:
            if todo.get("completed") is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE_LIST.append(todo.get("title"))
            TOTAL_NUMBER_OF_TASKS += 1
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for TASK_TITLE in TASK_TITLE_LIST:
        print("\t {}".format(TASK_TITLE))
