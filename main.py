# from functions import get_todos , write_todos
import functions

# todos = []
while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # match user_action:
    #     case 'add':
    if user_action.startswith('add'):  # 'add' in user_action:
        # todo = input("Enter a todo: ") + "\n"

        todo = user_action[4:]
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # with context manager
        todos = functions.get_todos()

        todos.append(todo + '\n')

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        # with open('todos.txt', 'w') as file:
        #     file.writelines(todos)
        functions.write_todos(todos)

        # case 'show':
    elif user_action.startswith('show'):  # 'show' in user_action:
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = functions.get_todos()

        # new_todos =[]
        # for new_item in todos:
        #     new_item = new_item.strip('\n')
        #     new_todos.append(new_item)

        # list-comprehension

        # new_todos = [new_item.strip('\n') for new_item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item.title()}"
            print(row)
        # case 'edit':
    elif user_action.startswith('edit'):  # 'edit' in user_action:
        try:
            # number = int(input("Number of to do to edit: "))
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            # with open('todos.txt', 'w') as file:
            #     file.writelines(todos)

            functions.write_todos(todos)

        except ValueError:
            print("Your command is invalid, edit will accept number only.")
            continue

        # case 'complete':
    elif user_action.startswith('complete'):  # 'complete' in user_action:
        try:
            # number = int(input("Number of the todo to complete:"))
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            # with open('todos.txt', 'w') as file:
            #     file.writelines(todos)

            functions.write_todos(todos)

            message = f"Todos {todo_to_remove} is completed."
            print(message)

        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print("It will accept number only.")
            continue

        # case 'exit':
    elif user_action.startswith('exit'):  # 'exit' in user_action:
        break
    else:
        print("Hey, you have entered a wrong command")

print("Bye!")
