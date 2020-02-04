#!/usr/bin/python3
""" Export to JSON """
if __name__ == "__main__":
    id_ = argv[1]
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    todo = requests.get(url_todo, params={'userId': id_})
    user = requests.get(url_user, params={'id': id_})

    todo_dict_list = todo.json()
    user_dict_list = user.json()
    task_list = []
    user_tasks = {}
    employee = user_dict_list[0].get('username')

    with open("{}.json".format(id_), "w+") as jsonfile:
        for task in todo_dict_list:
            status = task.get('completed')
            title = task.get('title')
            task_dict = {}
            task_dict['task'] = title
            task_dict['completed'] = status
            task_dict['username'] = employee
            task_list.append(task_dict)
        user_tasks[id_] = task_list

        data = json.dumps(user_tasks)
        jsonfile.write(data)
