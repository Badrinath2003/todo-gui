import streamlit as st

import tkinter as tk

if 'todos' not in st.session_state:
    try:
        with open("todos.txt", 'r') as file:
            st.session_state.todos = file.readlines()
    except FileNotFoundError:
        st.session_state.todos = []

def write_todos(todos):
    with open("todos.txt", 'w') as file:
        file.writelines(todos)

st.title("TODOs App")

user_action = st.selectbox("Choose an action", ["Add", "Show", "Edit", "Complete", "Exit"])

if user_action == 'Add':
    todo = st.text_input("Enter a todo:")
    if st.button("Add Todo"):
        if todo:
            st.session_state.todos.append(todo + "\n")
            write_todos(st.session_state.todos)
            st.success("Todo added!")
            st.experimental_rerun()

elif user_action == 'Show':
    if st.button("Show Todos"):
        st.write("Your Todos:")
        for index, item in enumerate(st.session_state.todos):
            st.write(f"{index + 1} - {item.strip()}")

elif user_action == 'Edit':
    if st.session_state.todos:
        number = st.number_input("Number of the todo to edit:", min_value=1, max_value=len(st.session_state.todos), step=1)
        new_todo = st.text_input("Enter the new todo:")
        if st.button("Edit Todo"):
            st.session_state.todos[number - 1] = new_todo + "\n"
            write_todos(st.session_state.todos)
            st.success("Todo edited!")
            st.experimental_rerun()
    else:
        st.warning("No todos to edit.")

elif user_action == 'Complete':
    if st.session_state.todos:
        number = st.number_input("Number of the todo to complete:", min_value=1, max_value=len(st.session_state.todos), step=1)
        if st.button("Complete Todo"):
            st.session_state.todos.pop(number - 1)
            write_todos(st.session_state.todos)
            st.success("Todo completed and removed!")
            st.experimental_rerun()
    else:
        st.warning("No todos to complete.")

elif user_action == 'Exit':
    st.stop()
