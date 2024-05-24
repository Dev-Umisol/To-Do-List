#understanding python interface via tkinter

import tkinter as tk

def AddTask():
    task = entry.get()

    if task:
        todoList.insert(tk.END, task)
        entry.delete(0, tk.END) #clear entry

#Title
root = tk.Tk()
root.title("To-Do List")

#Size of To-Do List Frame
frame = tk.Frame(root)
frame.pack(padx = 20, pady = 20)

#Size for entry boxes
entry = tk.Entry(frame, width = 30)
entry.grid(row = 0, column = 0, padx = 5, pady = 5)

#Add Button
addBtn = tk.Button(frame, text = "Add Task", command = AddTask)
addBtn.grid(row = 0, column = 1, padx = 5, pady = 5)

#Display Area
todoList = tk.Listbox(frame, width = 40, height = 10)
todoList.grid(row = 1, columnspan = 2, padx = 5, pady = 5)

root.mainloop()