import streamlit as st
from dataflow.dataflow import Dataflow

# Fake task storage in session
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("🗂️ Task Dashboard (Dummy App)")

dataflow = Dataflow()

dummy_3 = dataflow.secret("news_api_key")
st.write("dummy global secret is:", dummy_3)
dummy_4 = dataflow.variable("dummy_variable")
st.write("dummy local secret is:", dummy_4)

# Task input
with st.form("task_form"):
    task = st.text_input("Enter a new task")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])
    submitted = st.form_submit_button("Add Task")
    if submitted and task:
        st.session_state.tasks.append({"task": task, "priority": priority})

st.header("📋 Your Tasks")

# Filter section
priority_filter = st.selectbox("Filter by priority", ["All", "Low", "Medium", "High"])
if priority_filter != "All":
    filtered_tasks = [t for t in st.session_state.tasks if t["priority"] == priority_filter]
else:
    filtered_tasks = st.session_state.tasks

# Display table
if filtered_tasks:
    for i, t in enumerate(filtered_tasks, 1):
        st.write(f"{i}. {t['task']} — *{t['priority']}*")
else:
    st.write("No tasks to show.")
