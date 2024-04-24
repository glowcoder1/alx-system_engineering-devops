#!/usr/bin/python3
""" Export api to csv"""
import csv
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    request_url = 'https://jsonplaceholder.typicode.com/users'
    user = requests.get('{}/{}'.format(request_url, user_id)).json()
    user_name = user.get('username')
    tasks = requests.get('{}/{}/todos'.format(request_url, user_id)).json()

    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(['User ID', 'Username', 'Completed', 'Task Title'])
        for task in tasks:
            completed = str(task.get('completed'))
            task_title = str(task.get('title'))
            csv_writer.writerow([user_id, user_name, completed, task_title])
