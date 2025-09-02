

import streamlit as st

# App title
st.title("📝 Simple To-Do List App")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add a new task
new_task = st.text_input("Add a new task:")

if st.button("Add Task"):
    if new_task.strip() != "":
        st.session_state.tasks.append(new_task.strip())
        st.success(f"Task '{new_task}' added!")
    else:
        st.error("Please enter a task.")

# Display tasks
st.subheader("Your Tasks:")

for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([0.8, 0.2])
    col1.write(f"{i+1}. {task}")
    if col2.button("Done", key=f"done_{i}"):
        # Remove the task without rerun
        st.session_state.tasks.pop(i)
        # st.experimental_rerun()  # Optional: only if using updated Streamlit


