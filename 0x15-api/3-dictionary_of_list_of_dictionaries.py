#!/usr/bin/python3
"""
Script to export data in the JSON format
"""

import json
import requests

if __name__ == "__main__":
    todo_api_url = "https://jsonplaceholder.typicode.com/todos"
    todo_response = requests.get(todo_api_url).json()
    user_api_url = "https://jsonplaceholder.typicode.com/users/"
    user_response = requests.get(user_api_url).json()
    new_dict = {}
    for user in user_response:
        usrId = user.get("id")
        task_list = []
        for todo in todo_response:
            list_dict = {}
            if todo.get("userId") == usrId:
                list_dict["username"] = user.get("username")
                list_dict["task"] = todo.get("title")
                list_dict["completed"] = todo.get("completed")
                task_list.append(list_dict)
        new_dict[usrId] = task_list
    with open("todo_all_employees.json".format(usrId), mode='w') as file:
        json.dump(new_dict, file)
