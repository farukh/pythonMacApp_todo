import FreeSimpleGUI as sg
label = sg.Text("Type In A To-Do")
input_text = sg.InputText(tooltip="Enter todo here...")
add_button = sg.Button("Add ToDo")
window = sg.Window('My TO DO App', layout=[[label], [input_text, add_button]])
window.read()
