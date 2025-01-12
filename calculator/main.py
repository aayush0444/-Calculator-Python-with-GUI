from tkinter import *
import os
from PIL import Image, ImageTk

# Create main window
window_root = Tk()
window_root.minsize(733, 434)

#changing colour of main window


# Gathering directory of the file system
directory = os.getcwd()
window_root.title(directory)

# Creating an empty string to show up on the calculator entry window
input_val = StringVar()
input_val.set("")

# Creating a click event handler for buttons
def click(event):
    # Creating conditions for deleting the text inputs
    if event.widget.cget('text') == 'C':
        input_val.set("")
    elif event.widget.cget('text') == '=':
        try:
            result = eval(input_val.get())
            input_val.set(result)
        except Exception as e:
            input_val.set("Error")
    elif event.widget.cget('text') == 'DEL':
        current_value = input_val.get()
        new_value = current_value[:-1]
        input_val.set(new_value)
    else:
        button_event = event.widget.cget('text')
        new_value = input_val.get() + button_event
        input_val.set(new_value)
        print(button_event)

# Creating a heading for the window named calculator
heading = Label(window_root, text='Calculator', font=('Helvetica', 30, 'bold'), foreground='green')
heading.pack(pady=10)

# Creating an entry widget to display the button text
user_input = Entry(window_root, textvariable=input_val, font='arial 30 bold', width=22, bd=3, relief=SUNKEN, justify=RIGHT)
user_input.pack(pady=10)

# Creating the main container frame
main_frame = Frame(window_root)
main_frame.pack(pady=10, padx=10, fill='both', expand=True)

# Creating the left frame for buttons
left_frame = Frame(main_frame, bg='lightgrey')
left_frame.pack(side=LEFT, padx=5, pady=5, fill=Y)

# Creating frame_window1 inside left_frame
frame_window1 = Frame(left_frame, bg='lightgrey')
frame_window1.pack(pady=5)

# Creating buttons within frame_window1
button9 = Button(frame_window1, text='9', font='arial 25 bold', padx=22, pady=28)
button9.pack(pady=5, padx=15, side=LEFT)
button9.bind("<Button-1>", click)

button8 = Button(frame_window1, text='8', font='arial 25 bold', padx=22, pady=28)
button8.pack(pady=5, padx=15, side=LEFT)
button8.bind("<Button-1>", click)

button7 = Button(frame_window1, text='7', font='arial 25 bold', padx=22, pady=28)
button7.pack(pady=5, padx=15, side=LEFT)
button7.bind("<Button-1>", click)

# Creating frame_window2 inside left_frame
frame_window2 = Frame(left_frame, bg='lightgrey')
frame_window2.pack(pady=5)

button6 = Button(frame_window2, text='6', font='arial 25 bold', padx=22, pady=28)
button6.pack(pady=5, padx=15, side=LEFT)
button6.bind("<Button-1>", click)

button5 = Button(frame_window2, text='5', font='arial 25 bold', padx=22, pady=28)
button5.pack(pady=5, padx=15, side=LEFT)
button5.bind("<Button-1>", click)

button4 = Button(frame_window2, text='4', font='arial 25 bold', padx=22, pady=28)
button4.pack(pady=5, padx=15, side=LEFT)
button4.bind("<Button-1>", click)

# Creating frame_window3 inside left_frame
frame_window3 = Frame(left_frame, bg='lightgrey')
frame_window3.pack(pady=5)

button3 = Button(frame_window3, text='3', font='arial 25 bold', padx=22, pady=28)
button3.pack(pady=5, padx=15, side=LEFT)
button3.bind("<Button-1>", click)

button2 = Button(frame_window3, text='2', font='arial 25 bold', padx=22, pady=28)
button2.pack(pady=5, padx=15, side=LEFT)
button2.bind("<Button-1>", click)

button1 = Button(frame_window3, text='1', font='arial 25 bold', padx=22, pady=28)
button1.pack(pady=5, padx=15, side=LEFT)
button1.bind("<Button-1>", click)

# Creating frame_window4 inside left_frame
frame_window4 = Frame(left_frame, background='lightgrey')
frame_window4.pack(pady=5)

button0 = Button(frame_window4, text='0', font='arial 25 bold', padx=22, pady=28)
button0.pack(pady=5, padx=15, side=LEFT)
button0.bind("<Button-1>", click)

buttondel = Button(frame_window4, text='DEL', font='arial 25 bold', padx=22, pady=28)
buttondel.pack(pady=5, padx=15, side=LEFT)
buttondel.bind("<Button-1>", click)

# Creating right side frame for additional buttons
frame_right = Frame(main_frame, bg='lightgrey')
frame_right.pack(side=RIGHT, pady=5, padx=15, fill=Y)

# Creating buttons in right frame
button_add = Button(frame_right, text='+', font='arial 25 bold', padx=22, pady=10)
button_add.pack(pady=5, padx=15)
button_add.bind("<Button-1>", click)

button_sub = Button(frame_right, text='-', font='arial 25 bold', padx=22, pady=10)
button_sub.pack(pady=5, padx=15)
button_sub.bind("<Button-1>", click)

button_mult = Button(frame_right, text='*', font='arial 25 bold', padx=22, pady=10)
button_mult.pack(pady=5, padx=15)
button_mult.bind("<Button-1>", click)

button_div = Button(frame_right, text='/', font='arial 25 bold', padx=22, pady=10)
button_div.pack(pady=5, padx=15)
button_div.bind("<Button-1>", click)

button_result = Button(frame_right, text='=', font='arial 25 bold', padx=22, pady=10)
button_result.pack(pady=5, padx=15)
button_result.bind("<Button-1>", click)

button_c = Button(frame_right, text='C', font='arial 25 bold', padx=22, pady=10)
button_c.pack(pady=5, padx=15)
button_c.bind("<Button-1>", click)

# Creating a main loop for the window
window_root.mainloop()
