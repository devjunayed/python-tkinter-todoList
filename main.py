from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


root = Tk()
root.title("To-Do List")
root.geometry("400x650+500+50")
root.resizable(0, 0)

task_list = []

# function for clearing all item
def allClear():
    global task_list
    task_list.clear()
    with open("tasklist.txt", "w") as taskfile:
        taskfile.write(f"")
    listbox.delete(0, END)

# Showing alert during delete all item
def allClearAlert():
    sidebar.place_forget()
    result = messagebox.askquestion(
        "Are you sure?", "All items will be deleted and can't be restore!")
    if result == "yes":
        allClear()

# info box
def infoBox():
    sidebar.place_forget()
    messagebox.showinfo("About the Application", "Modified by: Md Junayed and Abdullah Al Noman(Fahim)\n\nInspired by: Parvat Computer Technology\n\nlink: https://www.youtube.com/watch?v=T60cEaVYMJE\n")
    


# Function will trigger when the add button is clicked
def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)


# deleting a single task
def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)

# opening file and showing task line by line
def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file = open('tasklist.txt', 'w')
        file.close()

# import and append file
def importAppend():
    sidebar.place_forget()
    global task_list
    filepath = filedialog.askopenfilename(
        initialdir="/Desktop", title="Choose file",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    with open(filepath, "r") as taskfile:
        tasks = taskfile.readlines()

    for task in tasks:
        if task != '\n':
            task_list.append(task)
            listbox.insert(END, task)
            with open("tasklist.txt", 'a') as taskfile:
                taskfile.write(f"\n{task}")

# clear and Import file
def clearImport():
    sidebar.place_forget()
    global task_list
    allClear()

    filepath = filedialog.askopenfilename(
        initialdir="/Desktop", title="Choose file",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    with open(filepath, "r") as taskfile:
        tasks = taskfile.readlines()

    for task in tasks:
        if task != '\n':
            task_list.append(task)
            listbox.insert(END, task)
            with open("tasklist.txt", 'a') as taskfile:
                taskfile.write(f"\n{task}")

# exiting manin window
def exit():
    root.destroy()

# sidebar state
def sidebarExpand():
    sidebar.place(x=0, y=0)
def sidebarCollapse():
    sidebar.place_forget()




#design start here
# icon
Image_icon = PhotoImage(file="Image/task.png")
root.iconphoto(False, Image_icon)

# top bar
TopImage = PhotoImage(file="Image/topbar.png")
Label(root, image=TopImage).pack()

# Dock icon
dockImage = PhotoImage(file="Image/dock.png")
dockButton = Button(root, width=30, height=30, image=dockImage,
                    bg="#32405b", fg="white", command=sidebarExpand, cursor="hand2")
dockButton.place(x=30, y=25)

# note icon
noteImage = PhotoImage(file="Image/task.png")
Label(root, image=noteImage, bg="#32405b").place(x=340, y=25)

heading = Label(root, text="All Task", font="Arial 20 bold",
                fg="white", bg="#32405b")
heading.place(x=130, y=25)


# main
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20 bold", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

addButton = Button(frame, text="Add", font="arial 20 bold", width=6,
                bg="#5a95ff", fg="#fff", bd=0, cursor="hand2", command=addTask)
addButton.place(x=300, y=0)

# list box
listBoxFrame = Frame(root, bd=3, width=700, height=280, bg="#32405b")
listBoxFrame.pack(pady=(160, 0))

listbox = Listbox(listBoxFrame, font=('arial', 12), width=40, height=16,
                  bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(listBoxFrame)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


openTaskFile()

# delete
Delete_icon = PhotoImage(file="Image/close.png")
Button(root, image=Delete_icon, bd=0, cursor="hand2",
       command=deleteTask).place(x=160, y=580)

# Sidebar
sidebar = Frame(root, bg="lightGray", width=200, height=650)
sidebar.place(x=0, y=0)
sidebar.place_forget()

# close button
Button(sidebar, text="x", font="arial 16 bold", bd=0, bg="lightGray",
       command=sidebarCollapse, cursor="hand2").place(x=155, y=10)
# import and append file
Button(sidebar, text="Import and Append", anchor="w", width=20, bd=0, bg="#32405b",
       fg="white", font="arial 12 bold", cursor="hand2", command=importAppend).place(x=0, y=50)
# import and clear item
Button(sidebar, text="Clear and Import", anchor="w", width=20, bd=0, bg="#32405b",
       fg="white", font="arial 12 bold", cursor="hand2", command=clearImport).place(x=0, y=80)
# clear all  item
Button(sidebar, text="Delete all", anchor="w", width=20, bd=0, bg="#32405b", fg="white",
       font="arial 12 bold", cursor="hand2", command=allClearAlert).place(x=0, y=110)


# info box
Button(sidebar, text="INFO", anchor="center", width=20, bd=0, bg="#32405b", fg="white",
       font="arial 12 bold", cursor="hand2", command=infoBox).place(x=0, y=580)


# Exit
Button(sidebar, text="EXIT", anchor="center", width=20, bd=0, bg="#32405b", fg="white",
       font="arial 12 bold", cursor="hand2", command=exit).place(x=0, y=610)


root.mainloop()
