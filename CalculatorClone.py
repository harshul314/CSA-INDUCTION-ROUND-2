from tkinter import *

root = Tk()
root.title("Calculator clone")

e = Entry(root, borderwidth=5, width=40)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

global operation

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))


def button_clear():
    e.delete(0, END)

def button_add():
    global operation
    operation = "addition"
    first_number = int(e.get())
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
    


def button_subtract():
    global operation
    operation = "subtraction"
    first_number = int(e.get())
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
    

def button_multiply():
    global operation
    operation = "multiplication"
    first_number=int(e.get())
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
   

def button_divide():
    global operation
    operation = "division"
    first_number = int(e.get())
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
   

def button_equal():
    second_number = int(e.get())
    e.delete(0, END)

    if operation == "addition":
        e.insert(0,f_num + second_number)
    elif operation == "subtraction":
        e.insert(0,f_num - second_number)
    elif operation == "multiplication":
        e.insert(0,f_num * second_number)
    elif operation == "division":
        e.insert(0, f_num/ second_number)





button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)

button_clear = Button(root, text="Clear", padx=79, pady=20, command = button_clear)
button_add = Button(root, text="+", padx=40, pady=20,command = button_add)
button_equal = Button(root, text="=", padx=184, pady=20, command = button_equal)
button_subtract = Button(root, text= "-", padx = 40, pady = 20, command = button_subtract)
button_divide = Button(root, text= "/", padx = 40, pady = 20, command = button_divide)
button_multiply = Button(root, text= "x", padx = 40, pady = 20, command = button_multiply)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row = 4, column = 3)
button_equal.grid(row=5, column=0, columnspan=4)
button_divide.grid(row = 1, column= 3)
button_multiply.grid(row = 2, column = 3)
button_subtract.grid(row = 3, column = 3)


root.mainloop()
#Made By - Harshul Dua