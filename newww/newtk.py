import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x500")
name = ttk.Label(text="Dec > Hex")
name.place(x=50, y=5)
decToHex = ttk.Entry()
decToHex.place(x=130, y=5)
def func():
    try:
        a = int(decToHex.get())
        resHex['text'] = "Result: " + str(hex(a))[2:].upper()
    except:
        resHex["text"] = "Try again"
convToHex = ttk.Button(text="Convert: ", command=func)
convToHex.place(x=50, y=30)
resHex = ttk.Label(text="Result:   ")
resHex.place(x=130, y=30)

#DEC TO HEX

name2 = ttk.Label(text="Dec > Hex")
name2.pack()
hexTodec = ttk.Entry()
hexTodec.place(x=130, y=50)
def func2():
    try:
        resdec['text'] = "Result: " + str(int(hexTodec.get(), 16))
    except:
        resdec["text"] = "Try again"
convTodec = ttk.Button(text="Convert: ", command=func2)
convTodec.pack()
resdec = ttk.Label(text="Result:   ")
resdec.pack()

#binary

name3 = ttk.Label(text="Dec > bin")
name3.pack()
decTobin = ttk.Entry()
decTobin.pack()
def func3():
    try:
        resbin['text'] = "Result: " + str(bin(int(decTobin.get()))[2:])
    except:
        resbin["text"] = "Try again"
convTobin = ttk.Button(text="Convert: ", command=func3)
convTobin.pack()
resbin = ttk.Label(text="Result:   ")
resbin.pack()


#dec
name4 = ttk.Label(text="bin > dex")
name4.pack()
binTodec = ttk.Entry()
binTodec.pack()
def func3():
    try:
        resbindec['text'] = "Result: " + str(int(binTodec.get()))
    except:
        resbindec["text"] = "Try again"
convTobindec = ttk.Button(text="Convert: ", command=func3)
convTobindec.pack()
resbindec = ttk.Label(text="Result:   ")
resbindec.pack()

root.mainloop()