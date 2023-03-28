from tkinter import *
from tkinter import ttk

import ptrace.debugger


root = Tk()

root.title("Memory I/O")
root.geometry("250x200")


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

    labelData['text'] = data


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

root.mainloop()

