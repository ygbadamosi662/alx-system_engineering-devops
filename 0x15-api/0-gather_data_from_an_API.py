#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com'

    employee_url = f'{base_url}/users/{sys.argv[1]}'
    response = requests.get(employee_url)
    if response.status_code != 200:
        print(f"Failed to retrieve employee details for ID: {sys.argv[1]}")
        return

    employee_data = response.json()
    employee_name = employee_data['name']

    todos_url = f'{base_url}/todos?userId={sys.argv[1]}'
    response = requests.get(todos_url)
    if response.status_code != 200:
        print(f"Failed to retrieve TODO list for employee: {employee_name}")
        return

    todos_data = response.json()
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    num_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks "
          f"({num_done_tasks}/{total_tasks}):")

    for task in done_tasks:
        task_title = task['title']
        print(f"\t {task_title}")
