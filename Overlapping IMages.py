from PIL import Image
img=Image.open('ADU.jpg')
img1=Image.open('DUDE.jpg')
area=(0,0,10,10)
img.paste(img1,area)
img.show()