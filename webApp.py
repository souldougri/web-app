import streamlit as St
import fuctiones

todos = fuctiones.get_todos()

def new_todo():
    newToDo = St.session_state["new_todo"] + '\n'
    todos.append(newToDo)
    fuctiones.write_todos(todos)
      # Rerun the app to update the list

St.title('To-Do App')
St.write("Save Your Time")

# Display each to-do item with a checkbox
for index, todo in enumerate(todos):
    if St.checkbox(todo, key=f'todo_{index}'):
        todos.pop(index)
        fuctiones.write_todos(todos)
        del St.session_state[f'todo_{index}']
        St.rerun()

# Add a text input and button to add new tasks
St.text_input(label="",
              placeholder="New to do...",
              on_change=new_todo,
              key="new_todo")
