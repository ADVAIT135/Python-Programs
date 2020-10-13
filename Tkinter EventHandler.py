from tkinter import *
root=Tk()
can_width=300
can_height=200
root.geometry(f"{can_width}x{can_height}")
root.title("Event handling")
win=Button(root,text="Click me")
win.pack()
i=0
def me(event):
    global i
    Label(root,text=f"You clicked me {i} time").pack()
    Label(root,text="Double click to exit screen").pack()
    i=i+1
win.bind("<Button-1>", me)
win.bind("<Double-1>", quit)
root.mainloop()
