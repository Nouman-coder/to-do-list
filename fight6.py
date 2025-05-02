import streamlit as st

# Initialize session state list if not already present
if "todo_list" not in st.session_state:
    st.session_state.todo_list = ["clean", "room", "study"]

def add_task(task):
    if task:
        st.session_state.todo_list.append(task)

def remove_task(task):
    if task in st.session_state.todo_list:
        st.session_state.todo_list.remove(task)

def main():
    st.title("📝 TO-DO LIST")

    st.write("### Current Tasks:")
    st.write(st.session_state.todo_list)

    option = st.radio("Select an option", ["Add Task", "Remove Task"])

    if option == "Add Task":
        new_task = st.text_input("Enter a task to add:")
        if st.button("Add"):
            add_task(new_task)
            st.success(f"'{new_task}' has been added.")

    elif option == "Remove Task":
        task_to_remove = st.selectbox("Select a task to remove:", st.session_state.todo_list)
        if st.button("Remove"):
            remove_task(task_to_remove)
            st.success(f"'{task_to_remove}' has been removed.")

if __name__ == "__main__":
    main()
