import tkinter as tk
from tkinter import *
from tkinter import ttk
import GUI_Solid

zas = GUI_Solid.filtration_significant_masses()
root = Tk()
my_tree = ttk.Treeview(root)
root.title('Solidworks Vibration Analysis Filter')
root.geometry('650x800')
root.resizable(False, False)
style = ttk.Style(root)
style.configure("Treeview", rowheight=30)


my_tree = ttk.Treeview(root)

#Define columns
my_tree['columns'] = ('Mass X', 'Mass Y', 'Mass Z')

#Formate our columns
my_tree.column('#0', width=120, anchor=CENTER)
my_tree.column("Mass X", anchor=CENTER, width=120)
my_tree.column("Mass Y", anchor=CENTER, width=120)
my_tree.column("Mass Z", anchor=CENTER, width=120)

#create Headings
my_tree.heading("#0", text='Frequency', anchor=CENTER)
my_tree.heading("Mass X", text='Mass X', anchor=CENTER)
my_tree.heading("Mass Y", text='Mass Y', anchor=CENTER)
my_tree.heading("Mass Z", text='Mass Z', anchor=CENTER)

#Add Data
for i in range(len(zas[1])):
    my_tree.insert(parent='', index='end', iid=i, text=zas[0][i], values=(zas[1][i], zas[2][i], zas[3][i]))

#pack to the screen
my_tree.pack(pady= 100, fill='y')

root.mainloop()





# win = Tk()
# frm = Frame(win)
# frm.pack(side=tk.LEFT, padx=20)
#
# tv = ttk.Treeview(frm, columns =(1,2,3,4), show = "headings", height='5')
# tv.pack()
# columns = 1
# tv.heading(1, text = "Częstotliwość [Hz]")
# tv.heading(2, text = "Share mass X axe")
# tv.heading(3, text = "Share mass Y axe")
# tv.heading(4, text = "Share mass Z axe")
# tv.insert()
#
#
#
# win.title("Solidworks Vibration Analysis Filter")
# win.geometry('850x500')
# win.resizable(False, False)
# win.mainloop()



