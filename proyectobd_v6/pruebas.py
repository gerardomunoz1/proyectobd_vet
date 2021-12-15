from tkinter import *
from tkinter import ttk
from database import Database


# Function for checking the
# key pressed and updating
# the listbox
def checkkey(event):
    value = event.widget.get()
    print(value)

    # get data from l
    if value == '':
        data = l
    else:
        data = []
        for item in l:
            if value.lower() in item.lower():
                data.append(item)

    # update data in listbox
    update(data)


def update(data):
    # clear previous data
    lb.delete(0, 'end')

    # put new data
    for item in data:
        lb.insert('end', item)


# Driver code
l = ['C', 'C++', 'Java',
     'Python', 'Perl',
     'PHP', 'ASP', 'JS']

root = Tk()

# creating text box
e = Entry(root)
e.pack()
e.bind('<KeyRelease>', checkkey)

# creating list box
lb = ttk.Combobox(root)
lb["values"] = l
lb.pack()
update(l)

root.mainloop()
