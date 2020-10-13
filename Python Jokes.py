import tkinter as tk
import pyjokes
root=tk.Tk()
root.geometry("360x100")
root.title("FUN GAME")
T=tk.Text(root,height=4,width=80)
T.pack()

def generatejoke():
    global joke
    joke=pyjokes.get_joke()
    T.insert(tk.END,joke)
    
b=tk.Button(text="JOKE",command=generatejoke)
b.pack()
root.mainloop()