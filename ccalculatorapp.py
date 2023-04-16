from tkinter import *
from tkinter import messagebox

root = Tk()
###USING TITLE BARS TO PROVIDE TITLE
root.title("SIMPLE CALCULATOR")
##USING THIS TO CHANGE THE ICON OF THE APP
root.iconbitmap(r'C:\Users\test001\Downloads\calculator.png')
##USING ENTRY BARS TO PROVIDE THE ENTRY TO ENTER THE INFORMATION LIKE SEEARCH BARS
e = Entry(root, width=70, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
##USING STATUS BARS
status = Label(root, text="CALCI STATUS", bd=1, relief=SUNKEN)
status.grid(row=7, column=1)


##USING BUTTONADD FUNCTON TO PROVIDE FUNCTIONALITY TO KEYS IN CALCI
def button_add(number):
    ##TO GET THE VALUE FROM THE ENTRY BOX WE USE E.GET METHOD

    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+ str(number))
    # e.insert(0,str(number))

def button_addition():
    try:
        first_number = e.get()
        global f_num
        global math
        math = "addition"
        f_num = int(first_number)
        e.delete(0, END)
    except ValueError:
        messagebox.showerror("ERROR", "ENTER THE VALUE FIRST")
        # print("ENTER THE VALUE FIRST")


##USING BUTTON EQUAL FUNCTION TO PROVIDE EQUALITY FUNCTION TO GIVEN AND TO PERFORM TASKS...
def button_equal():
    try:
        second_number = e.get()
        e.delete(0, END)
        if math == "addition":
            e.insert(0, f_num + int(second_number))
            status = Label(root, text="CALCI WORKED ON ADDITION", bd=1, relief=SUNKEN)
            status.grid(row=7, column=1)

        if math == "subtraction":
            e.insert(0, f_num - int(second_number))
            status = Label(root, text="CALCI WORKED ON  SUBTRACTION", bd=1, relief=SUNKEN)
            status.grid(row=7, column=1)
        if math == "multipy":
            e.insert(0, f_num * int(second_number))
            status = Label(root, text="CALCI WORKED ON MULTIPLICATION", bd=1, relief=SUNKEN)
            status.grid(row=7, column=1)
        if math == "divison":
            e.insert(0, f_num / int(second_number))
            status = Label(root, text="CALCI WORKED ON DIVISION", bd=1, relief=SUNKEN)
            status.grid(row=7, column=1)
    except NameError:
        ##MESSAGEBOX IS USED TO SHOW THE POP-UP MESSAGE
        messagebox.showerror("ERROR", "ENTER THE VALUES AND OPERATION TOO THEN USE EQUAL TOO")
        print("ENTER THE VALUES AND OPERATION TOO THEN RUN EQUAL TOO")
    except ValueError:
        messagebox.showerror("ERROR", "MISSING VALUES")
        # print("ENTERED ONLY ONE VALUE ")

##TO PERFORM SUB OPEREATION AND TO PROVIDE FUCTIONALITY TO BUTTON
def button_subtraction():
    try:
        first_number = e.get()
        global f_num
        global math
        math = "subtraction"
        f_num = int(first_number)
        e.delete(0, END)
    except ValueError:
        messagebox.showerror("ERROR", "ENTER THE VALUE FIRST")
        # print("ENTER THE VALUE FIRST")


##TO PERFORM MUL OPEREATION AND TO PROVIDE FUCTIONALITY TO BUTTON
def button_multipy():
    try:
        first_number = e.get()
        global f_num
        global math
        math = "multipy"
        f_num = int(first_number)
        e.delete(0, END)
    except ValueError:
        messagebox.showerror("ERROR", "ENTER THE VALUES FIRST")
        # print("ENTER THE VALUE FIRST")

##TO PERFORM DIV OPEREATION AND TO PROVIDE FUCTIONALITY TO BUTTON
def button_divison():
    try:
        first_number = e.get()
        global f_num
        global math
        math = "divison"
        f_num = int(first_number)
        e.delete(0, END)
    except ValueError:
        messagebox.showerror("ERROR", "ENTER THE VALUES FIRST")
        # print("ENTER THE VALUE FIRST")


def button_clear():

        response = messagebox.askyesno("warning", "ARE YOU SURE YOU WANT TO CLEAR ?")
        # Label(root, text=respons)
        if response == 1:
            e.delete(0, END)

        else:
            pass






def quit():
    response = messagebox.askyesno("warning", "ARE YOU SURE YOU WANT TO EXIT ?")
    # Label(root, text=response).pack
    if response == 1:
        root.quit()
    else:
        pass


##CREATING BUTTONS AND ASSIGNING FUNCTIONALTY USING BUTTON KEYWORD
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_add(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_add(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_add(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_add(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_add(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_add(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_add(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_add(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_add(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_add(0))

button_addi = Button(root, text="+", padx=39, pady=20, command=button_addition)
button_equal = Button(root, text="=", padx=39, pady=20, command=button_equal)
button_sub = Button(root, text="-", padx=39, pady=20, command=button_subtraction)
button_multipy = Button(root, text="X", padx=39, pady=20, command=button_multipy)
button_division = Button(root, text="%", padx=39, pady=20, command=button_divison)
button_clear = Button(root, text="CLEAR", padx=80, pady=20, command=button_clear)


button_quit = Button(root, text="EXIT CALCI", padx=80, pady=20, command=quit)

##CREATING GRIDS (TO STRUCTURE THE KEYWORDS BUTTONS)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)


button_clear.grid(row=6, column=0)
button_equal.grid(row=4, column=1)
button_addi.grid(row=4, column=2)
button_sub.grid(row=5, column=2)
button_multipy.grid(row=5, column=1)
button_division.grid(row=5, column=0)
button_sub.grid(row=5, column=2)
button_quit.grid(row=6, column=2)

root.mainloop()
