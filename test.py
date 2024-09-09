import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        my_listbox1.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        my_listbox3.insert(tk.END, task)

def delete_task():
    selected_task = my_listbox1.curselection()
    if selected_task:
        my_listbox1.delete(selected_task)


def mark_task():
    selected_task = my_listbox1.curselection()
    if selected_task:
        my_listbox2.insert(tk.END, my_listbox1.get(selected_task))
        my_listbox1.delete(selected_task)

root = tk.Tk()
root.title('My List')
root.configure(background='SlateGray4')

label_style = {'bg': 'SlateGray4', 'fg': 'white', 'font': ('Arial', 12, 'bold')}

label = tk.Label(root, text='Enter your items:', **label_style)
label.pack(pady=(20, 5), padx=20)

task_entry = tk.Entry(root, width=40, bg='LightGoldenrod1', fg='grey1', font=('Arial', 10))
task_entry.pack(pady=10, padx=20)

button_style = {'bg': 'SteelBlue3', 'fg': 'grey1', 'font': ('Arial', 10, 'bold'), 'width': 15}

add_task_button = tk.Button(root, text='Add', **button_style, command=add_task)
add_task_button.pack(pady=(5, 5))

del_task_button = tk.Button(root, text='Delete', **button_style, command=delete_task)
del_task_button.pack(pady=(5, 5))

mark_task_button = tk.Button(root, text='Mark', **button_style, command=mark_task)
mark_task_button.pack(pady=(5, 10))

label2 = tk.Label(root, text='Your tasks', **label_style)
label2.pack(pady=(20, 5), padx=20)

my_listbox1 = tk.Listbox(root, width=50, height=6, bg='LightGoldenrod1', fg='grey1', font=('Arial', 10))
my_listbox1.pack(pady=(0, 20))

label3 = tk.Label(root, text='Completed tasks', **label_style)
label3.pack(pady=(10, 5), padx=20)

my_listbox2 = tk.Listbox(root, width=50, height=6, bg='LightGoldenrod1', fg='grey1', font=('Arial', 10))
my_listbox2.pack(pady=(0, 20))

label4 = tk.Label(root, text='Archived tasks', **label_style)
label4.pack(pady=(10, 5), padx=20)

my_listbox3 = tk.Listbox(root, width=50, height=6, bg='LightGoldenrod1', fg='grey1', font=('Arial', 10))
my_listbox3.pack(pady=(0, 20))

root.mainloop()

