from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, save, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        # file = open("todos.txt", "r")
        # todos = file.readlines()
        # file.close()

        todos = get_todos()

        todos.append(todo + "\n")

        # file = open("todos.txt", "w")
        # file.writelines(todos)
        # file.close()

        write_todos("todos.txt", todos)

    elif user_action.startswith("show"):
        # file = open("todos.txt", "r")
        # todos = file.readlines()
        # file.close()

        todos = get_todos()

        new_todos = [item.strip('\n') for item in todos]

        print(todos)
        for index, item in enumerate(new_todos):
            row = f"{index+1} - {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number-1] = new_todo + "\n"

            write_todos("todos.txt", todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            todo_to_remove = todos[number-1].strip("\n")

            todos.pop(number-1)
            write_todos("todos.txt", todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("save"):
        with open("list.txt","w") as our_list:
            our_list.writelines(todos)

    elif 'exit' in user_action:
        break
    else:
        print("Entry is not valid")

print("Bye")