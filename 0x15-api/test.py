#!/usr/bin/python3

if __name__ == "__main__":
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    todos = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()
    done_tasks = [task.get('title') for task in todos if task.get('completed') is True]
    print('Employee {} is done with tasks({}/{}):'.format(
        user.get('name'), len(done_tasks), len(todos)))
    [print('\t {}'.format(tsk)) for tsk in done_tasks if True]
