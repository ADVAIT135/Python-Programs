"""NAME : ADVAIT GURUNATH CHAVAN, PRN: 4119008, S.E. ELECTRONICS, SEM 4, TW-10"""

""" Program to create a GUI with three buttons of different color. On the click of button  the background color should
 as per the color of the button using Frame class of Tkinter"""

from tkinter import *
from tkinter import messagebox

root = Tk()
blank_space = ' '
title = 'COLOR BUTTONS'
root.title(15 * blank_space + title)
messagebox.showinfo(" Welcome to color buttons program", "Hi ADVAIT,click on each color button and you will see the "
                                                         "window color changing to the color specified on the button. "
                                                         "Click on Ok or close this window to continue.....")


def red_button_clicked():
    messagebox.showinfo("RED BUTTON CLICKED", "Hi ADVAIT you just clicked on RED button. Now click on the Ok button "
                                              "or close this window to make the window appear red")
    root.configure(bg='red')


def blue_button_clicked():
    messagebox.showinfo("BLUE BUTTON CLICKED", "Hi ADVAIT you just clicked on BLUE button. Now click on the Ok button "
                                               "or close this window to make the window appear blue")
    root.configure(bg='blue')


def yellow_button_clicked():
    messagebox.showinfo("YELLOW BUTTON CLICKED", "Hi ADVAIT you just clicked on YELLOW button. Now click on the Ok "
                                                 "button or close this window to make the window appear yellow")
    root.configure(bg='yellow')


def green_button_clicked():
    messagebox.showinfo("GREEN BUTTON CLICKED", "Hi ADVAIT you just clicked on GREEN button. Now click on the Ok "
                                                "button or close this window to make the window appear green")
    root.configure(bg='green')


class ColorButton:
    def __init__(self, root1):
        self.f = Frame(root1, height=500, width=900)
        self.f.propagate(0)
        self.b1 = Button(root1, text='RED', command=red_button_clicked, activeforeground='red', activebackground='pink',
                         height=1,
                         width=10, font='algerian', bd=4)

        self.b2 = Button(root1, text='BLUE', command=blue_button_clicked, activeforeground='blue',
                         activebackground='pink',
                         height=1,
                         width=10, font='algerian', bd=4)

        self.b3 = Button(root1, text='YELLOW', command=yellow_button_clicked, activeforeground='yellow',
                         activebackground='pink',
                         height=1, width=10, font='algerian', bd=4)

        self.b4 = Button(root1, text='GREEN', command=green_button_clicked, activeforeground='green',
                         activebackground='pink',
                         height=1, width=10, font='algerian', bd=4)
        self.b1.pack(side=LEFT)
        self.b2.pack(side=TOP)
        self.b3.pack(side=RIGHT)
        self.b4.pack(side=BOTTOM)


mb = ColorButton(root)
root.mainloop()
