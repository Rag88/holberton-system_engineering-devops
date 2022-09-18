#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    usrId = int(argv[1])
    todo_api_url = "https://jsonplaceholder.typicode.com/todos"
    todo_response = requests.get(todo_api_url).json()
    user_api_url = "https://jsonplaceholder.typicode.com/users/{}".\
        format(usrId)
    user_response = requests.get(user_api_url).json()
    task_list = []
    for todo in todo_response:
        list_dict = {}
        if todo.get("userId") == usrId:
            list_dict["task"] = todo.get("title")
            list_dict["completed"] = todo.get("completed")
            list_dict["username"] = user_response.get("username")
            task_list.append(list_dict)
        new_dict = {usrId: task_list}
    with open("{}.json".format(usrId), mode='w') as file:
        json.dump(new_dict, file)
