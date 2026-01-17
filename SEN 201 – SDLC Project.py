import tkinter as tk
from tkinter import messagebox

# -------------------------------
# Application Data
# -------------------------------
tasks = []

# -------------------------------
# Core SDLC Functions
# -------------------------------
def add_task():
    task = task_entry.get()
    if task == "":
        messagebox.showwarning("Input Error", "Please enter a task")
        return
    tasks.append({"task": task, "completed": False})
    task_entry.delete(0, tk.END)
    update_task_list()

def complete_task():
    selected = task_list.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a task")
        return
    index = selected[0]
    tasks[index]["completed"] = True
    update_task_list()

def update_task_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        status = "✔ Done" if task["completed"] else "⏳ Pending"
        task_list.insert(tk.END, f"{task['task']} - {status}")

# -------------------------------
# GUI Setup
# -------------------------------
root = tk.Tk()
root.title("Student Task Management System")
root.geometry("500x400")
root.configure(bg="#f4f6f8")

# -------------------------------
# Styling
# -------------------------------
PRIMARY_BLUE = "#2563eb"
HOVER_BLUE = "#1e40af"

def on_enter(e):
    e.widget["background"] = HOVER_BLUE

def on_leave(e):
    e.widget["background"] = PRIMARY_BLUE

# -------------------------------
# UI Components
# -------------------------------
title = tk.Label(
    root,
    text="Student Task Management System",
    font=("Segoe UI", 16, "bold"),
    bg="#f4f6f8"
)
title.pack(pady=10)

task_entry = tk.Entry(root, font=("Segoe UI", 11), width=35)
task_entry.pack(pady=10)

add_btn = tk.Button(
    root,
    text="Add Task",
    bg=PRIMARY_BLUE,
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    width=20,
    command=add_task
)
add_btn.pack(pady=5)

add_btn.bind("<Enter>", on_enter)
add_btn.bind("<Leave>", on_leave)

task_list = tk.Listbox(
    root,
    font=("Segoe UI", 10),
    width=45,
    height=10
)
task_list.pack(pady=10)

complete_btn = tk.Button(
    root,
    text="Mark as Completed",
    bg=PRIMARY_BLUE,
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    width=20,
    command=complete_task
)
complete_btn.pack(pady=5)

complete_btn.bind("<Enter>", on_enter)
complete_btn.bind("<Leave>", on_leave)

# -------------------------------
# Run Application
# -------------------------------
root.mainloop()
