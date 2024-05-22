#!/usr/bin/python3
"""display all the todo lists of employees tasks done"""

import requests
import sys


if __name__ == '__main__':
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    employeeId = sys.argv[1]
    url = baseUrl + "/" + employeeId

    csv_file_path = (f"{employeeId}.csv")

    response = requests.get(url)
    employUsername = response.json().get('username')

    todo_url = url + '/todos'
    response_2 = requests.get(todo_url)
    all_tasks = response_2.json()

    with open(csv_file_path, "w") as data_file:
        for task in all_tasks:
            completed = task.get('completed')
            title = task.get('title')
            data_file.write(
                f'"{employeeId}","{employUsername}","{completed}","{title}"\n')
