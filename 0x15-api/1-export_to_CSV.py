#!/usr/bin/python3
""" CSV format."""
import csv
import requests
import sys

if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         sys.argv[1]).json()

    do = requests.get('https://jsonplaceholder.typicode.com/todos/?userId=' +
                      sys.argv[1]).json()

    username = users.get('username')

    with open(sys.argv[1] + '.csv', mode='w') as csv_file:
        write = csv.writer(csv_file, delimiter=',', quotechar='"',
                           quoting=csv.QUOTE_ALL)
        for data in do:
            write.writerow([sys.argv[1], username, data.get("completed"),
                            data.get("title")])
