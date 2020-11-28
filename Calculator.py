from tkinter import *
from functools import partial

def button_pressed(value):
    expression_field_value.set(expression_field_value.get() + str(value))

def equal_pressed():
    try:
        result = eval(expression_field_value.get())
        expression_field_value.set(result)
    except ZeroDivisionError:
        expression_field_value.set("Division by zero error. Clear to continue.")

def clear_pressed():
    expression_field_value.set("")

if __name__ == "__main__":
    window = Tk()
    window.title("My Little Calculator")

    expression_field_value = StringVar()
    expression_field = Entry(window, width=30, textvariable=expression_field_value)
    expression_field.grid(row=0, column=0, columnspan=4)

    when_pressed = partial(button_pressed, "1")
    button1 = Button(window, text="1", height=3, width=3, borderwidth=1, command=when_pressed)
    button1.grid(row=1, column=0, sticky="ew")

    when_pressed = partial(button_pressed, "2")
    button2 = Button(window, text="2", height=3, width=3, borderwidth=1, command=when_pressed)
    button2.grid(row=1, column=1, sticky="ew")

    when_pressed = partial(button_pressed, "3")
    button3 = Button(window, text="3", height=3, width=3, borderwidth=1, command=when_pressed)
    button3.grid(row=1, column=2, sticky="ew")

    when_pressed = partial(button_pressed, "*")
    multiplication = Button(window, text="*", height=3, width=3, borderwidth=1, command=when_pressed)
    multiplication.grid(row=1, column=3, sticky="ew")

    when_pressed = partial(button_pressed, "4")
    button4 = Button(window, text="4", height=3, width=3, borderwidth=1, command=when_pressed)
    button4.grid(row=2, column=0, sticky="ew")

    when_pressed = partial(button_pressed, "5")
    button5 = Button(window, text="5", height=3, width=3, borderwidth=1, command=when_pressed)
    button5.grid(row=2, column=1, sticky="ew")

    when_pressed = partial(button_pressed, "6")
    button6 = Button(window, text="6", height=3, width=3, borderwidth=1, command=when_pressed)
    button6.grid(row=2, column=2, sticky="ew")

    when_pressed = partial(button_pressed, "-")
    subtraction = Button(window, text="-", height=3, width=3, borderwidth=1, command=when_pressed)
    subtraction.grid(row=2, column=3, sticky="ew")

    when_pressed = partial(button_pressed, "7")
    button7 = Button(window, text="7", height=3, width=3, borderwidth=1, command=when_pressed)
    button7.grid(row=3, column=0, sticky="ew")

    when_pressed = partial(button_pressed, "8")
    button8 = Button(window, text="8", height=3, width=3, borderwidth=1, command=when_pressed)
    button8.grid(row=3, column=1, sticky="ew")

    when_pressed = partial(button_pressed, "9")
    button9 = Button(window, text="9", height=3, width=3, borderwidth=1, command=when_pressed)
    button9.grid(row=3, column=2, sticky="ew")

    when_pressed = partial(button_pressed, "+")
    addition = Button(window, text="+", height=3, width=3, borderwidth=1, command=when_pressed)
    addition.grid(row=3, column=3, sticky="ew")

    when_pressed = partial(button_pressed, "0")
    button0 = Button(window, text="0", height=3, width=3, borderwidth=1, command=when_pressed)
    button0.grid(row=4, column=0, sticky="ew")

    equal_button = Button(window, text="=", height=3, width=3, borderwidth=1, command=equal_pressed)
    equal_button.grid(row=4, column=1, sticky="ew")

    clear_button = Button(window, text="C", height=3, width=3, borderwidth=1, command=clear_pressed)
    clear_button.grid(row=4, column=2, sticky="ew")

    when_pressed = partial(button_pressed, "/")
    division = Button(window, text="/", height=3, width=3, borderwidth=1, command=when_pressed)
    division.grid(row=4, column=3, sticky="ew")

    window.mainloop()
