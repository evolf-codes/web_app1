FILEPATH = "todos.txt"
def get_todo_list(filepath=FILEPATH):
    """Read a text file and return the list
    of to-do items
    """
    with open(filepath) as file:
        todo_list_local = file.readlines()
    return todo_list_local

#print(help(get_todo_list))
def write_todos(todos_arg, filepath=FILEPATH):
    """Write item in to-do list into the text file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    '''
    this will only run if we run functions.py to test it
    if we run it as a module, it will change the name to functions and not run
    '''
    print("HELLO")