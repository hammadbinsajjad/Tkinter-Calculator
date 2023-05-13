from tkinter import *

window = Tk()

window.geometry("370x450")
window.configure(bg="#3399ff")
window.title("Calculator")

# Frames
expression_frame = Frame(window, bg="#3399FF")
buttons_frame = Frame(window, bg="#3399FF")
expression_frame.pack()
buttons_frame.pack()

# Widgets

# Equation input
font_entry = ("arial", 20, "bold")
equation = StringVar()
equation.set("0")
equation_field = Entry(expression_frame, textvariable=equation, font=font_entry, justify="right")
equation_field.pack(pady=20, ipadx=10, ipady=10, fill=X)

expression = ""


def press(n):
    global expression
    expression += str(n)
    equation.set(expression)


def evaluate():
    global expression
    try:
        result = eval(equation.get())
        equation.set(result)
    except ZeroDivisionError as ze:
        equation.set("Math Error")
    expression = ""


def clear_entry():
    global expression
    expression = ""
    equation.set("0")


def backspace_entry():
    global expression
    expression = expression.rstrip(expression[-1])
    if not expression:
        equation.set("0")
    else:
        equation.set(expression)


# Buttons
font_button = ("times new roman", 12)
button0 = Button(buttons_frame, text="0", font=font_button, relief="ridge", bg="#80BFFF", borderwidth=1,
                 width=8, height=3, command=lambda: press("0"))
button1 = Button(buttons_frame, text="1", font=font_button, relief="ridge", bg="#80BFFF", borderwidth=1,
                 width=8, height=3, command=lambda: press("1"))
button2 = Button(buttons_frame, text="2", font=font_button, relief="ridge", bg="#80BFFF", borderwidth=1,
                 width=8, height=3, command=lambda: press(2))
button3 = Button(buttons_frame, text="3", font=font_button, relief="ridge", bg="#80BFFF", borderwidth=1,
                 width=8, height=3 , command=lambda: press(3))
button4 = Button(buttons_frame, text="4", font=font_button, relief="ridge", bg="#80BFFF", borderwidth=1,
                 width=8, height=3, command=lambda: press(4))
button5 = Button(buttons_frame, text="5", font=font_button, relief="ridge", bg="#80BFFF", borderwidth=1,
                 width=8, height=3, command=lambda: press(5))
button6 = Button(buttons_frame, text="6", font=font_button, relief="ridge", bg="#80BFFF", borderwidth=1,
                 width=8, height=3, command=lambda: press(6))
button7 = Button(buttons_frame, text="7", font=font_button, relief="ridge", bg="#80BFFF", borderwidth=1,
                 width=8, height=3, command=lambda: press(7))
button8 = Button(buttons_frame, text="8", font=font_button, relief="ridge", bg="#80BFFF", borderwidth=1,
                 width=8, height=3, command=lambda: press(8))
button9 = Button(buttons_frame, text="9", font=font_button, relief="ridge", bg="#80BFFF", borderwidth=1,
                 width=8, height=3, command=lambda: press(9))

plus = Button(buttons_frame, text="+", font=font_button, relief="ridge", bg="#80BFFF", borderwidth=1,
              width=8, height=3, command=lambda: press("+"))
minus = Button(buttons_frame, text="-", font=font_button, relief="ridge", bg="#80BFFF", borderwidth=1,
               width=8, height=3, command=lambda: press("-"))
multiply = Button(buttons_frame, text="*", font=font_button, relief="ridge", bg="#80BFFF", borderwidth=1,
                  width=8, height=3, command=lambda: press("*"))
divide = Button(buttons_frame, text="/", font=font_button, relief="ridge", bg="#80BFFF", borderwidth=1,
                width=8, height=3, command=lambda: press("/"))
decimal = Button(buttons_frame, text=".", font=font_button, relief="ridge", bg="#80BFFF", borderwidth=1,
                 width=8, height=3, command=lambda: press("."))
clear = Button(buttons_frame, text="C", font=font_button, relief="ridge", bg="#80BFFF", borderwidth=1,
               width=8, height=3, command=clear_entry)
equal = Button(buttons_frame, text="=", font=font_button, relief="ridge", bg="#80BFFF", borderwidth=1,
               width=8, height=3, command=evaluate)
backspace = Button(buttons_frame, text="<", font=font_button, relief="ridge", bg="#80BFFF", borderwidth=1,
                   width=8, height=3, command=backspace_entry)

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
plus.grid(row=0, column=3)

button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
minus.grid(row=1, column=3)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
multiply.grid(row=2, column=3)

button0.grid(row=3, column=0)
decimal.grid(row=3, column=1)
clear.grid(row=3, column=2)
divide.grid(row=3, column=3)

equal.grid(row=4, column=0, columnspan=3, sticky="nsew")
backspace.grid(row=4, column=3)

window.mainloop()
