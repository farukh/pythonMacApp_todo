import streamlit as sl
import functions

todos = functions.get_todo()
def add_todo():
    todo = sl.session_state['new_todo']+ '\n'
    todos.append(todo)
    functions.write_todo(todos)

sl.title("My Todo Web App")
sl.subheader("This is ToDo App")
sl.write("This App is to increase your productivity. ")

for index,todo in enumerate(todos):
    sl.checkbox(todo,key=index)

sl.text_input(label="Enter ToDo.",
              placeholder="Enter ToDo and press Enter/Return",
              on_change=add_todo, key='new_todo')