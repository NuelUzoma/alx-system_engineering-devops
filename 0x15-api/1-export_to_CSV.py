#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the CSV format.
Requirements:
Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""


if __name__ == "__main__":
    import csv
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
    # write to CSV file
    file_name = "{}.csv".format(EMPLOYEE_ID)
    with open(file_name, 'w', newline='') as csvfile:
        headers = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, headers=headers)
        writer.writeheader()
        # write each task as a row in csv file
        for task in todos:
            task_title = task.get('title')
            task_status = 'COMPLETE' if task in completed_tasks else 'INCOMPLETE'
            writer.writerow({"USER_ID": EMPLOYEE_ID, "USERNAME": user.get('name'),
             "TASK_COMPLETED_STATUS": task_status, "TASK_TITLE": task_title})
    # show results
    print(
        "Employee {} is done with tasks({}/{}). CSV file created: {}".format(
    user.get('name'), len(completed_tasks), number_total_tasks, file_name))
