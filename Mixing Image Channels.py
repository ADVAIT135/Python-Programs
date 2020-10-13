from PIL import Image
img=Image.open('ADU.jpg')
r,g,b=img.split()
img1=Image.merge("RGB",(r,r,b))
img1.show()