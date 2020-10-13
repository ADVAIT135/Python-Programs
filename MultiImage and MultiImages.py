from PIL import Image
img=Image.open('ADU.jpg')
img1=Image.open('DUDE.jpg')
r1,g1,b1=img.split()
r2,g2,b2=img1.split()
mix_image=Image.merge("RGB",(r2,g1,b2))
mix_image.show()