#!/usr/bin/python3

"""Gather data from an API  for a given employee ID"""
import requests
import sys


BASE_URL = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        if id:
            employee = requests.get('{}/users/{}'.format(BASE_URL, id)).json()
            employee_name = employee.get('name')
            tasks = requests.get('{}/todos?userId={}'
                                 .format(BASE_URL, id)).json()
            completed_tasks = [task for task in tasks if task.get("completed")]
            print('Employee {} is done with tasks({}/{}):'
                  .format(employee_name, len(completed_tasks),
                          len(tasks)))
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get("title")))
