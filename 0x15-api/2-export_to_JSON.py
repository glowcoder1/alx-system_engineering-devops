#!/usr/bin/python3
"""Exports data in the JSON format to {userId}.json"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId)).json()

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(userId)
    url = url + '/todos/'
    tasks = requests.get(url).json()
    taskList = []
    users = {}

    for task in tasks:
        taskList.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user.get('username')
        })

    users[userId] = taskList

    with open('{}.json'.format(userId), mode='w') as f:
        json.dump(users, f)
