5



from tkinter import *

win = Tk()
win.title("Calculator")
win.geometry("360x650")   
def addValue(n):
    e1.insert(END, n)

def calculate():
    try:
        ans = eval(e1.get())
        e1.delete(0, END)
        e1.insert(0, ans)
    except:
        e1.delete(0, END)
        e1.insert(0, "Error")

def backspace():
    eq = e1.get()
    e1.delete(0, END)
    e1.insert(0, eq[:-1])

# Entry box 
e1 = Entry(win, font=("calibri", 24), bd=10, justify="right")
e1.grid(column=0, row=0, columnspan=4, padx=10, pady=15, ipady=10)

btn_params = {"font": ("calibri", 20), "width": 4, "height": 2, "bd": 5}

# Row 1 
Button(win, text="/", command=lambda: addValue("/"), **btn_params).grid(row=1, column=0, padx=5, pady=5)
Button(win, text="*", command=lambda: addValue("*"), **btn_params).grid(row=1, column=1, padx=5, pady=5)
Button(win, text="-", command=lambda: addValue("-"), **btn_params).grid(row=1, column=2, padx=5, pady=5)
Button(win, text="+", command=lambda: addValue("+"), **btn_params).grid(row=1, column=3, padx=5, pady=5)

# Row 2
Button(win, text="9", command=lambda: addValue("9"), **btn_params).grid(row=2, column=0, padx=5, pady=5)
Button(win, text="8", command=lambda: addValue("8"), **btn_params).grid(row=2, column=1, padx=5, pady=5)
Button(win, text="7", command=lambda: addValue("7"), **btn_params).grid(row=2, column=2, padx=5, pady=5)
Button(win, text="<-", command=backspace, **btn_params).grid(row=2, column=3, padx=5, pady=5)

# Row 3
Button(win, text="6", command=lambda: addValue("6"), **btn_params).grid(row=3, column=0, padx=5, pady=5)
Button(win, text="5", command=lambda: addValue("5"), **btn_params).grid(row=3, column=1, padx=5, pady=5)
Button(win, text="4", command=lambda: addValue("4"), **btn_params).grid(row=3, column=2, padx=5, pady=5)
Button(win, text="=", command=calculate, **btn_params).grid(row=3, column=3, padx=5, pady=5, rowspan=2, sticky="ns")

# Row 4
Button(win, text="3", command=lambda: addValue("3"), **btn_params).grid(row=4, column=0, padx=5, pady=5)
Button(win, text="2", command=lambda: addValue("2"), **btn_params).grid(row=4, column=1, padx=5, pady=5)
Button(win, text="1", command=lambda: addValue("1"), **btn_params).grid(row=4, column=2, padx=5, pady=5)

# Row 5
Button(win, text="0", command=lambda: addValue("0"), **btn_params).grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")
Button(win, text=".", command=lambda: addValue("."), **btn_params).grid(row=5, column=2, padx=5, pady=5)
Button(win, text="C", command=lambda: e1.delete(0, END), **btn_params).grid(row=5, column=3, padx=5, pady=5)

win.mainloop()
