from tkinter import *
from tkinter import ttk

import ptrace.debugger
import psutil


mem_var = 0

root = Tk()

root.title("Memory I/O")
root.geometry("200x230")


def read():
    pid = int(entryPID.get())
    address = entryAddress.get()
    a = int(address, 16)

    print(pid)
    print(type(pid))
    print(address)
    print(a)
    print(type(a))

    p = ptrace.debugger.PtraceDebugger()
    process = p.addProcess(pid, False)
    data = process.readWord(a)
    process.detach()

    labelData['text'] = "Data = <" + str(data) + ">"


def write():
    pid = int(entryPID.get())
    address = entryAddress.get()
    a = int(address, 16)

    newData = int(entryNewData.get())

    print(pid)
    print(type(pid))
    print(address)
    print(a)
    print(type(a))

    p = ptrace.debugger.PtraceDebugger()
    process = p.addProcess(pid, False)
    process.writeWord(a, newData)
    process.detach()


labelPID = ttk.Label(text="PID:")
labelPID.pack()

entryPID = ttk.Entry()
entryPID.pack()

labelAddres = ttk.Label(text="Address:")
labelAddres.pack()

entryAddress = ttk.Entry()
entryAddress.pack()

buttonRead = ttk.Button(text='Read', command=read)
buttonRead.pack()

labelData = ttk.Label(text="Data = <>")
labelData.pack()

labelNewData = ttk.Label(text="New data:")
labelNewData.pack()

entryNewData = ttk.Entry()
entryNewData.pack()

buttonWrite = ttk.Button(text='Write', command=write)
buttonWrite.pack()

labelMem = ttk.Label(text='Max mem = <%>')
labelMem.pack(expand=1, anchor=S)

def update_maxMem():
    global mem_var
    global root

    now = psutil.virtual_memory()[2]

    if now > mem_var:
        mem_var = now
        labelMem["text"] = "Max mem = <" + str(mem_var) + "%>"

    root.after(1000, update_maxMem)

update_maxMem()

root.mainloop()

