#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
Requirements:
You must use urllib or requests module
The script must accept an integer as a parameter, which is the employee ID
The script must display on the standard output the employee
TODO list progress in this exact format:
First line: Employee EMPLOYEE_NAME is done with tasks
(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks,
which is the sum of completed and non-completed tasks
Second and N next lines display the title of completed tasks: TASK_TITLE
(with 1 tabulation and 1 space before the TASK_TITLE)
"""

if __name__ == "__main__":
    import requests
    import sys

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
