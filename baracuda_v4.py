from tkinter import *
import tkinter as tk
from tkinter import ttk
import random
import test_2

root = Tk()
root.title('GUI Solidworks Analysis Data')
root.geometry('650x500')
root.resizable(False, False)
my_tree = ttk.Treeview(root)

list1 = test_2.filtration_significant_masses()


list2 = [[],[],[],[]]
for i in range(4):
    for z in range(20):
        list2[i].append(random.randint(0,10))

def handle_click(event):
    if my_tree.identify_region(event.x, event.y) == "separator":
        return "break"

# Define columns
my_tree['columns'] = ('Frequency', 'Mass X', 'Mass Y', 'Mass Z')

# Formate our columns
my_tree.column('#0', width=0, stretch=NO)
my_tree.column('Frequency', anchor=CENTER, width=120)
my_tree.column("Mass X", anchor=CENTER, width=120)
my_tree.column("Mass Y", anchor=CENTER, width=120)
my_tree.column("Mass Z", anchor=CENTER, width=120)

my_tree.heading("#0", text='', anchor=CENTER)
my_tree.heading("Frequency", text='Frequency', anchor=CENTER)
my_tree.heading("Mass X", text='Mass X', anchor=CENTER)
my_tree.heading("Mass Y", text='Mass Y', anchor=CENTER)
my_tree.heading("Mass Z", text='Mass Z', anchor=CENTER)

my_tree.pack(pady=20, fill='y')

#Set entry
lbl = Label(root, text="Percent mass filter")
lbl.place(relx=0.1, rely=0.8, relwidth=0.15, relheight=0.04)

entry = tk.Entry(bg='white', font=('Segoe UI', 10), justify=CENTER)
entry.place(relx=0.1, rely=0.85, relwidth=0.15, relheight=0.04)

#Functions


#button add
button = tk.Button(text='list1', font=('Segoe UI', 10), command= lambda: list1_values(entry.get()))
button.place(relx=0.3, rely=0.85, relheight=0.05, relwidth=0.2)

#button add
button_2 = tk.Button(text='list2', font=('Segoe UI', 10), command= lambda: list2_values())
button_2.place(relx=0.5, rely=0.85, relheight=0.05, relwidth=0.2)

#table values
def list1_values(entry):
    if entry == '':
        my_tree.delete(*my_tree.get_children())
        #print
        for i in range(len(list1[0])):
            my_tree.insert(parent='', index='end', iid=i, text='',
                           values=(list1[0][i], list1[1][i], list1[2][i], list1[3][i]))
    elif entry.isdigit():
        my_tree.delete(*my_tree.get_children())
        #print(10*float(entry))
        #print('Haha')
        fl = [[], [], [], []]

        for u in range(len(list1[0])):
            if float(list1[1][u]) >= float(entry)/100 or float(list1[2][u]) >= float(entry)/100 or float(list1[3][u]) >= float(entry)/100:
                fl[0].append(list1[0][u])
                fl[1].append(list1[1][u])
                fl[2].append(list1[2][u])
                fl[3].append(list1[3][u])
        for h in range(len(fl[0])):
            my_tree.insert(parent='', index='end', iid=h, text='', values=(fl[0][h], fl[1][h], fl[2][h], fl[3][h]))
    else:
        lbl_error = Label(root, text="Input value is incorrect!", fg='red')
        lbl_error.place(relx=0.02, rely=0.9, relwidth=0.3, relheight=0.04)

def list2_values():
    my_tree.delete(*my_tree.get_children())
    for i in range(len(list2[0])):
        my_tree.insert(parent='', index='end', iid=i, text='', values=(list2[0][i], list2[1][i], list2[2][i], list2[3][i]))


my_tree.bind('<Button-1>', handle_click)
root.mainloop()