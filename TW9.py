"""NAME : ADVAIT GURUNATH CHAVAN, PRN : 4119008, S.E. ELECTRONICS, SEM 4, TW-9"""
"""Program to create a GUI image of a smiling face using Canvas class of Tkinter"""
from tkinter import *

root = Tk()
blank_space = ' '
title = "SMILING FACE"
root.title(190 * blank_space + title)
root.geometry('1000x650')
c = Canvas(root, height=650, width=1000, bg='light green')
c.create_text(650, 80, fill='dark red', font='Algerian', text='Hi, ADVAIT keep yourself smiling just like '
                                                              'this smiley.')
c.create_text(650, 110, fill='dark red', font='Algerian',
              text='No matter how big or difficult is the problem or assignment '
                   'or project be!!')
c.create_text(650, 610, fill='blue', font='Times',
              text='Made by: ADVAIT GURUNATH CHAVAN, PRN: 4119008, S.E. ELECTRONICS, SEM 4, MHSSCE.')
c.create_oval(5, 5, 250, 300, width=4, fill='yellow')
c.create_arc(15, 40, 105, 40, width=5, style='arc')
c.create_arc(105, 40, 200, 40, width=5, style='arc')
c.create_oval(50, 45, 100, 100, width=3, fill='white')
c.create_oval(60, 65, 90, 100, fill='black')
c.create_oval(70, 75, 80, 85, fill='white')
c.create_oval(155, 45, 205, 100, width=3, fill='white')
c.create_oval(165, 65, 195, 100, fill='black')
c.create_oval(175, 75, 185, 85, fill='white')
c.create_line(125, 100, 125, 220, width=4)
c.create_line(145, 200, 125, 100, width=4)
c.create_line(105, 200, 125, 100, width=4)
c.create_arc(105, 100, 145, 220, width=4, start=205, extent=125, style='arc')
c.create_line(50, 230, 209, 230, width=6)
arv2 = c.create_arc(49, 209, 210, 251, start=180, extent=180, fill='white')
c.create_arc(50, 189, 209, 263, width=8, start=180, extent=180, style='arc')
arc = c.create_arc(60, 210, 200, 263, start=180, extent=180, fill='red')
c.pack()
root.mainloop()
