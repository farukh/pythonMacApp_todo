import FreeSimpleGUI as sg
import functions
import time

sg.theme('Darkpurple4')
lblTodo = sg.Text("Enter Todo")
inputTodo = sg.InputText(tooltip="Enter Todo...", key='todo')
btnAddTodo = sg.Button(image_source='add.png', tooltip="Add ToDo",
                       size=2, mouseover_colors='LightBlue2', key='Add')
#   Edit Block
lbTodos = sg.Listbox(functions.get_todo(), size=[45, 10],
                     enable_events=True, key='todos')
btnEdit = sg.Button('Edit')
btnCompleted = sg.Button(image_source='complete.png', tooltip="Mark Complete..",
                         size=2, mouseover_colors='LightBlue2', key='Completed')
btnExit = sg.Button('Exit')
lblClock = sg.Text('Clock:', key='clock')
win = sg.Window("Todo Manager",
                layout=[[lblClock], [lblTodo], [inputTodo, btnAddTodo],
                        [lbTodos, btnEdit, btnCompleted],
                        [btnExit]], font=('Helvetica', 20))
EditMode = False
todo_for_edit = ""
while True:
    event, values = win.read(timeout=1000)
    win['clock'].update(time.strftime('%b %d %Y %H: %M: %S'))
    #print(f'1. {event}')
    #print(f'2. {values}')
    #print(EditMode)
    match event:
        case "Add":
            if EditMode == False:
                if values['todo'] == '':
                    sg.popup("Write ToDo First...", font=('Helvetica', 20))
                    continue
                todos = functions.get_todo()
                todo = values["todo"]
                todos.append(todo + "\n")
                functions.write_todo(todos)
                win['todos'].update(values=todos)
                win['todo'].update('')
            else:
                todos = functions.get_todo()
                todos[todos.index(todo_for_edit)] = values['todo']
                win['todos'].update(values=todos)
                EditMode = False
                todo_for_edit = ""
                win['Add'].update("Add")
                win['todo'].update('')
        case "Edit":
            try:
                todo_for_edit = values['todos'][0]
                win['todo'].update(todo_for_edit)
                win['Add'].update("Update")
                EditMode = True
            except:
                sg.popup("Please select ToDo item from list first...", font=('Helvetica', 20))
        case "Completed":
            try:
                todo_for_completed = values['todos'][0]
                todos = functions.get_todo()
                todos.remove(todo_for_completed)
                functions.write_todo(todos)
                win['todos'].update(values=todos)
            except:
                sg.popup("Please select ToDo item from list first...", font=('Helvetica', 20))

        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
win.Close()
