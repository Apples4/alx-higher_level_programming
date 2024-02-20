#!/usr/bin/python3
""" script that uses API method 'GET' """
import requests
import sys

if __name__ == '__main__': 
    user_id = int(sys.argv[1])

    """ fetch tasks for userid """
    respon = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
    todos = respon.json()

    total_todos = len(todos)
    done_todos = sum(1 for task in todos if task['completed'])

    """ fetch username from userid """
    respon = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    user_name = respon.json()['name']

    """ show progress """
    print(f'Employee {user_name} is done with tasks({done_todos}/{total_todos}):')
    for task in todos:
        if task['completed']:
            print(f"\t{task['title']}")
