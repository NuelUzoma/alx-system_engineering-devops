#!/usr/bin/python3

import requests
import sys

def gather_data():
    # get the employee ID from the command line
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[1]))
        sys.exit(1)
    EMPLOYEE_ID = sys.argv[1]

    # API Request
    URL = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(URL + 'users/{}'.format(EMPLOYEE_ID)).json()
    todos = requests.get(URL + 'todos', params={'userId': EMPLOYEE_ID}).json()
    completed_tasks = [task.get('title') for task in todos if task.get(
        'completed') is True]
    # number of completed tasks
    number_total_tasks = len(todos)
    # display results
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(completed_tasks), number_total_tasks))
    [print('\t {}'.format(tsk)) for tsk in completed_tasks if True]

if __name__ == "__main__":
    gather_data()