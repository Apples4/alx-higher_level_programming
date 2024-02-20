import csv
import requests
import sys


if __name__ == '__main__':
    user_id = int(sys.argv[1])

    """ Fetch tasks for userid """
    respon = requests.get(
                        f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
    todos = respon.json()

    total_todos = len(todos)
    done_todos = sum(1 for task in todos if task['completed'])

    """ Fetch username from userid """
    res = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    user_name = res.json()['name']

    """ creating a csv file """
    header_list = ["USER_ID",
                    "USERNAME",
                    "TASK_COMPLETED_STATUS",
                    "TASK_TITLE"]

    csv.register_dialect("myDialect",
                         delimiter=",",
                         quoting=csv.QUOTE_ALL)

    """ puting in the dict info into the csv file """
    with open("USER_ID.csv", "w", newline='') as file:
        writer = csv.DictWriter(file,
                                fieldnames=header_list,
                                dialect="myDialect")
        writer.writeheader()
        for task in todos:
            writer.writerow({
                             "USER_ID": user_id,
                             "USERNAME": user_name,
                             "TASK_COMPLETED_STATUS": task['completed'],
                             "TASK_TITLE": task['title']})
