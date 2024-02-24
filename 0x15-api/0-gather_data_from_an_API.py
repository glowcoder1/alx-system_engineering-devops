#!/usr/bin/python3
'''
Gather data from an API  for a given employee ID
'''

import re
import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            employee = requests.get('{}/users/{}'.format(BASE_URL, id)).json()
            tasks = requests.get('{}/todos?userId={}'
                                 .format(BASE_URL, id)).json()
            completed_tasks = [task for task in tasks if task["completed"]]
            print(
                f'Employee {employee["name"]} is done with tasks '
                f'({len(completed_tasks)}/{len(tasks)}):'
                )
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print(f'\t {task["title"]}')
