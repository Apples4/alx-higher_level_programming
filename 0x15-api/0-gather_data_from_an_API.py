import requests
import sys

if __name__ == '__main__': 
    user_id = int(sys.argv[1])

    # Fetch tasks for userid
    respon = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
    todos = respon.json()

    total_todos = len(todos)
    done_todos = sum(1 for task in todos if task['completed'])

    # Fetch username from userid
    res = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    user_name = res.json()['name']  # Corrected line

    # Show progress
    print(f'Employee {user_name} is done with tasks({done_todos}/{total_todos}):')
    for task in todos:
        if task['completed']:
            print(f"\t{task['title']}")
