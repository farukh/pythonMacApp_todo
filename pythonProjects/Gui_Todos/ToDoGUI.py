import FreeSimpleGUI as sg
import functions
lblTodo = sg.Text("Enter Todo")
inputTodo = sg.InputText(tooltip="Enter Todo...",key='todo')
btnAddTodo = sg.Button("Add")
#   Edit Block
lbTodos = sg.Listbox(functions.get_todo(), size=[45, 10],
                     enable_events=True, key='todos')
btnEdit = sg.Button('Edit')
win = sg.Window("Todo Manager",
                layout=[[lblTodo], [inputTodo, btnAddTodo],
                        [lbTodos, btnEdit]])
EditMode = False
todo_for_edit= ""
while True:
    event, values = win.read()
    print(f'1. {event}')
    print(f'2. {values}')
    print(EditMode)
    match event:
        case "Add":
            if EditMode==False:
                todos = functions.get_todo()
                todo = values["todo"]
                todos.append(todo+"\n")
                functions.write_todo(todos)
                win['todos'].update(values=todos)
                win['todo'].update('')
            else:
                todos = functions.get_todo()
                todos[todos.index(todo_for_edit)] = values['todo']
                win['todos'].update(values=todos)
                EditMode = False
                todo_for_edit=""
                win['Add'].update("Add")
                win['todo'].update('')
        case "Edit":
            todo_for_edit = values['todos'][0]
            win['todo'].update(todo_for_edit)
            win['Add'].update("Update")
            EditMode = True
        case sg.WIN_CLOSED:
            break
win.Close()