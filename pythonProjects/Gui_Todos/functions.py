def get_todo():
    with open('todos.txt', 'r') as file:
       todos = file.readlines()
    return todos


def write_todo(todo):
   with open('todos.txt', 'w') as file:
       file.writelines(todo)


