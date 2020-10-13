from PIL import Image
img=Image.open('ADU.jpg')
img1=Image.open('DUDE.jpg')
res_img=img.resize((200,200))
res2_img1=img1.resize((200,100))
img.show()
res_img.show()
img1.show()
res2_img1.show()