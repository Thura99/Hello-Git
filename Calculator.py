from tkinter import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("ERROR")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    gui = Tk()
    gui.configure(bg="light green")
    gui.title = "CALCULATOR"
    gui.geometry("370x180")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=10, padx=50)
    equation.set("ENTER")

    bt1 = Button(gui, text="1", fg="black", bg="red", command=lambda: press(1), height=1, width=8)
    bt1.grid(row=2, column=0)
    bt2 = Button(gui, text="2", fg="black", bg="red", command=lambda: press(2), height=1, width=8)
    bt2.grid(row=2, column=1)
    bt3 = Button(gui, text="3", fg="black", bg="red", command=lambda: press(3), height=1, width=8)
    bt3.grid(row=2, column=2)
    bt4 = Button(gui, text="4", fg="black", bg="red", command=lambda: press(4), height=1, width=8)
    bt4.grid(row=2, column=3)
    bt5 = Button(gui, text="5", fg="black", bg="red", command=lambda: press(5), height=1, width=8)
    bt5.grid(row=3, column=0)
    bt6 = Button(gui, text="6", fg="black", bg="red", command=lambda: press(6), height=1, width=8)
    bt6.grid(row=3, column=1)
    bt7 = Button(gui, text="7", fg="black", bg="red", command=lambda: press(7), height=1, width=8)
    bt7.grid(row=3, column=2)
    bt8 = Button(gui, text="8", fg="black", bg="red", command=lambda: press(8), height=1, width=8)
    bt8.grid(row=3, column=3)
    bt9 = Button(gui, text="9", fg="black", bg="red", command=lambda: press(9), height=1, width=8)
    bt9.grid(row=4, column=1)
    bt0 = Button(gui, text="0", fg="black", bg="red", command=lambda: press(0), height=1, width=8)
    bt0.grid(row=4, column=2)

    btp = Button(gui, text="+", fg="black", bg="blue", command=lambda: press("+"), height=1, width=8)
    btp.grid(row=5, column=0)
    btm = Button(gui, text="-", fg="black", bg="blue", command=lambda: press("-"), height=1, width=8)
    btm.grid(row=5, column=1)
    btu = Button(gui, text="*", fg="black", bg="blue", command=lambda: press("*"), height=1, width=8)
    btu.grid(row=5, column=2)
    btd = Button(gui, text="/", fg="black", bg="blue", command=lambda: press("/"), height=1, width=8)
    btd.grid(row=5, column=3)
    btp = Button(gui, text="%", fg="black", bg="blue", command=lambda: press("%"), height=1, width=8)
    btp.grid(row=6, column=1)
    bte = Button(gui, text="=", fg="black", bg="yellow", command=equalpress, height=1, width=8)
    bte.grid(row=6, column=2)
    btc = Button(gui, text="C", fg="black", bg="yellow", command=clear, height=1, width=8)
    btc.grid(row=6, column=0)
    btdd = Button(gui, text=".", fg="black", bg="red", command=lambda: press("."), height=1, width=8)
    btdd.grid(row=6, column=3)

    gui.mainloop()
