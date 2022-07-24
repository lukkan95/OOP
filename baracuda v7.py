from tkinter import *
import tkinter as tk
from tkinter import ttk
import csv
import unidecode
import tkinter.filedialog


root = Tk()
my_str = tk.StringVar()

root.title('GUI Vibration Analysis - CSV Files Filter')
root.geometry('650x500')
img = PhotoImage(file="untitled.png")  # Replace "image.png" with any image file.
root.iconphoto(False, img)
root.resizable(False, False)
my_tree = ttk.Treeview(root)


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

my_tree.pack(pady=40, fill='y')

#Set entry
lbl = Label(root, text="Percent mass filter")
lbl.place(relx=0.1, rely=0.8, relwidth=0.15, relheight=0.04)

entry = tk.Entry(bg='white', font=('Segoe UI', 10), justify=CENTER)
entry.place(relx=0.1, rely=0.85, relwidth=0.15, relheight=0.04)

#Functions


#button add
button = tk.Button(text='Apply', font=('Segoe UI', 10), command= lambda: list1_values(entry.get()))
button.place(relx=0.3, rely=0.85, relheight=0.05, relwidth=0.2)

# button add
# button_3 = tk.Button(text='Show all', font=('Segoe UI', 10), command= lambda: list2_values())
# button_3.place(relx=0.8, rely=0.7, relheight=0.05, relwidth=0.2)

entry2=tk.Entry(font=40)
entry2.place(relx=0.6, rely=0.85, relwidth=0.15, relheight=0.04)

button_2=tk.Button(root,text="DEM",font=40,command=lambda: browsefunc())
button_2.place(relx=0.8, rely=0.85, relheight=0.05, relwidth=0.2)


def browsefunc():
    global filename
    filename =tk.filedialog.askopenfilename(filetypes=(("csv files","*.csv"),("All files","*.*")))
    entry2.insert(tk.END, filename) # add this


def instantiate_from_csv():
    #vcs_file = str(input('Please enter path to vcs_file: '))
    vcs_file = filename
    with open(vcs_file, 'r') as f:
        reader = csv.reader(f)
        items = list(reader)
        return items

def frequency_validation():
    items = instantiate_from_csv()
    frequency_list = []
    for x in range(4, len(items)-1):
        frequency = str(items[x][1])
        frequency = unidecode.unidecode(frequency)
        frequency = frequency.replace(' ', '.')
        frequency = frequency.strip('.')
        frequency_list.append(frequency)
    return frequency_list


def mass_share_X_axe():
    items = instantiate_from_csv()
    mass_x_list = []
    for x in range(4, len(items) - 1):
        mass_x = str(items[x][2])
        mass_x = unidecode.unidecode(mass_x)
        mass_x = mass_x.replace(' ', '.')
        mass_x = mass_x.strip('.')
        mass_x_list.append(mass_x)

    return mass_x_list

def mass_share_Y_axe():
    items = instantiate_from_csv()
    mass_y_list = []
    for y in range(4, len(items) - 1):
        mass_y = str(items[y][3])
        mass_y = unidecode.unidecode(mass_y)
        mass_y = mass_y.replace(' ', '.')
        mass_y = mass_y.strip('.')
        mass_y_list.append(mass_y)

    return mass_y_list

def mass_share_Z_axe():
    items = instantiate_from_csv()
    mass_z_list = []
    for z in range(4, len(items) - 1):
        mass_z = str(items[z][4])
        mass_z = unidecode.unidecode(mass_z)
        mass_z = mass_z.replace(' ', '.')
        mass_z = mass_z.strip('.')
        mass_z_list.append(mass_z)

    return mass_z_list

def filtration_significant_masses():

        frequency = frequency_validation()
        x = mass_share_X_axe()
        y = mass_share_Y_axe()
        z = mass_share_Z_axe()
        list1 = [frequency, x, y, z]
        return list1

#table values
def list1_values(entry):
    list1 = filtration_significant_masses()
    if entry == '':
        my_tree.delete(*my_tree.get_children())
        for i in range(len(list1[0])):
            my_tree.insert(parent='', index='end', iid=str(i), text='',
                           values=(list1[0][i], list1[1][i], list1[2][i], list1[3][i]))
    elif entry.isdigit():
        my_tree.delete(*my_tree.get_children())
        fl = [[], [], [], []]
        for u in range(len(list1[0])):
            if float(list1[1][u]) >= float(entry)/100 or float(list1[2][u]) >= float(entry)/100 or float(list1[3][u]) >= float(entry)/100:
                fl[0].append(list1[0][u])
                fl[1].append(list1[1][u])
                fl[2].append(list1[2][u])
                fl[3].append(list1[3][u])
        for h in range(len(fl[0])):
            my_tree.insert(parent='', index='end', iid=str(h), text='', values=(fl[0][h], fl[1][h], fl[2][h], fl[3][h]))
    else:
        lbl_error = Label(root, text="Input value is incorrect!", fg='red')
        lbl_error.place(relx=0.02, rely=0.9, relwidth=0.3, relheight=0.04)


my_tree.bind('<Button-1>', handle_click)
root.mainloop()