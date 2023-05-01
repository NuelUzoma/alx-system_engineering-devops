#!/usr/bin/python3

import csv

gather_data = __import__('test2').gather_data

file_name = "{}.csv".format(gather_data.EMPLOYEE_ID)
with open(file_name, 'w', newline='') as csvfile:
    headers = [
        "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    # write each task as a row in csv file
    for task in gather_data.todos:
        task_title = task.get('title')
        task_sts = 'COMPLETE' if task in gather_data.completed_tasks else 'INCOMPLETE'
        writer.writerow(
            {"USER_ID": gather_data.EMPLOYEE_ID, "USERNAME": gather_data.user.get('name'),
                "TASK_COMPLETED_STATUS": task_sts, "TASK_TITLE": task_title})
    # show results
    print(
        "Employee {} is done with tasks({}/{}). CSV file created: {}".format(
            gather_data.user.get('name'), len(
                gather_data.completed_tasks), gather_data.number_total_tasks, file_name))