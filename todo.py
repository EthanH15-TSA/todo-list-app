# todo.py

# Step 1: Start with an empty list to hold tasks
tasks = []
completed_tasks=[]
# Step 2: Add a task
def add_task(task):
    tasks.append(task)

# Step 3: View tasks
def view_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}.{task}")

# Step 4: Delete a task
def delete_tasks(task_number):
    task = tasks.pop(task_number-1)
    print(f"Deleted: {task}")

# Step 5: Mark task complete
def mark_complete(task_number):
    task = tasks.pop(task_number-1)
    completed_tasks.append(task)
    print(f"Completed: {task}")
    print("Completed task list:")
    for i, task in enumerate(completed_tasks, start=1):
        print(f"{i}.{task}")


# Demo flow (you can run this file directly: python todo.py)
if __name__ == "__main__":
    add_task("Finish Cyber 201 assignment")
    add_task("Push code to GitHub")
    view_tasks()
    delete_tasks(1)
    mark_complete(1)
    view_tasks()
   # save_tasks()