from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import os


root = Tk()

root.title("File Browser")
root.geometry("200x230")

tv = None
checkCon = None

labelPath = ttk.Label(text="Path:")
labelPath.pack(fill=X)

entryPath = ttk.Entry()
entryPath.pack(fill=X)

def print_list(st=False):
    global entryPath
    global tv
    global entryCon

    a = os.listdir(path=entryPath.get())
    print(a)
    print(type(a))

    tv.delete(*tv.get_children())

    if st:
        print("check!!")
        l = []
        s = entryCon.get()

        if s == '':
            return

        c=0
        for x in a:
            if x[0] == s[0]:
                l.append(x)
            c += 1

        print(l)

        c=0
        for x in l:
            tv.insert(parent="", index=c, values=(x))
            c += 1

        
    else:
        print("not check!!")
        c=0
        for x in a:
            tv.insert(parent="", index=c, values=(x))
            c += 1
    

def openDir():
    global entryPath
    
    p = filedialog.askdirectory()
    print(p)
    entryPath.delete(0,END)
    entryPath.insert(0,p)
    print(entryPath.get())

    print_list()


buttonOpen = ttk.Button(text='Open dir...', command=openDir)
buttonOpen.pack()

labelCon = ttk.Label(text="Condition:")
labelCon.pack(fill=X)

entryCon = ttk.Entry()
entryCon.pack(fill=X)

def check():
    global checkCon
    print(checkCon.get())
    print_list(st=bool(checkCon.get()))


checkCon = IntVar()


checkbuttonCon = ttk.Checkbutton(text='Check condition?', variable=checkCon, command=check)
checkbuttonCon.pack()

tv = ttk.Treeview(columns=(1), show='headings')
tv.heading(1, text="files and dirs")
tv.insert(parent="", index=0, values=("test"))


tv.pack(fill=X)


root.mainloop()

