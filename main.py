while True:
    user_action = input("add, show , edit, completed exit : ")
    match user_action:
        case 'add':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todo = input("To-do: ")+"\n"
            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display' | 'view':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                print(f"{index+1}: {item.strip()}")
        case 'edit':
            itemNum = int(input("Which Item number you want to Edit: "))
            todos[itemNum-1] = input("Enter new To-do: ")
        case 'completed':
            itemNum = int(input("Which Item number you want to mark Completed: "))
            todos.pop(itemNum-1)
        case 'exit':
            break
        case anyVarName:
            print("You entered invalid case to match",anyVarName)
print('Bye')
