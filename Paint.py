from tkinter import *
import PIL
from PIL import Image,ImageDraw
def save():
    filename = 'image.png'
    image1.save(filename)
def point(event):
    x1,y1 = (event.x),(event.y)
    x2,y2 = (event.x+1),(event.y+1)
    cv.create_oval((x1,y1,x2,y2),fill='black',width=10)
    draw.line((x1,y1,x2,y2),fill='black',width=10)
root =  Tk()
cv= Canvas(root,width=640,height=480,bg='white')
image1 = PIL.Image.new('RGB',(640,480),'white')
draw = ImageDraw.Draw(image1)
cv.bind('<B1-Motion>',point)
cv.pack(expand=YES,fill=BOTH)
btn_save=Button(text="save",command=save)
btn_save.pack()
root.mainloop()