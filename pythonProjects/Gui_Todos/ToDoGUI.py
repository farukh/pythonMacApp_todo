import FreeSimpleGUI as sg
import functions
lblTodo = sg.Text("Enter Todo")
inputTodo = sg.InputText(tooltip="Enter Todo...",key='todo')
btnAddTodo = sg.Button("Add")

win = sg.Window("Todo Manager",layout=[[lblTodo,inputTodo,btnAddTodo]])
while True:
    event, values = win.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todo()
            todo = values["todo"]
            todos.append(todo+"\n")
            functions.write_todo(todos)
        case sg.WIN_CLOSED:
            break
win.Close()