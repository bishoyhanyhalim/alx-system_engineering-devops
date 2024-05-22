#!/usr/bin/python3
"""display all the todo lists of employees tasks done"""

import requests
import json
import sys


if __name__ == "__main__":
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    employ_id = sys.argv[1]
    url = baseUrl + "/" + employ_id

    json_file_path = (f"{employ_id}.json")

    response = requests.get(url)
    employ_username = response.json().get("username")

    tasks_url = url + "/todos"
    response_2 = requests.get(tasks_url)
    all_task = response_2.json()

    dictionary = {employ_id: []}

    for data in all_task:
        task_title = data.get('title')
        completed_status = data.get('completed')
        dictionary[employ_id].append({
            "task": task_title,
            "completed": completed_status,
            "username": employ_username,
        })

    with open(json_file_path, "w") as file_data:
        save = json.dump(dictionary, file_data)
