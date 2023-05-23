#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import csv
import requests
import sys

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com'

    employee_url = f'{base_url}/users/{sys.argv[1]}'
    response = requests.get(employee_url)
    if response.status_code != 200:
        print(f"Failed to retrieve employee details for ID: {sys.argv[1]}")

    employee_data = response.json()
    employee_username = employee_data['username']

    todos_url = f'{base_url}/todos?userId={sys.argv[1]}'
    response = requests.get(todos_url)
    if response.status_code != 200:
        print(f"Failed to retrieve TODO list for employee: {employee_name}")

    todos_data = response.json()

    csv_filename = f'{sys.argv[1]}.csv'

    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        for task in todos_data:
            task_completed_status = task['completed']
            task_title = task['title']
            writer.writerow([
                    f'{sys.argv[1]}',
                    f'{employee_username}',
                    f'{task_completed_status}',
                    f'{task_title}'
            ])

    print(f"CSV file '{csv_filename}' has been created.")
