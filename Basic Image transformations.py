from PIL import Image
img=Image.open('ADU.jpg')
img1=Image.open('DUDE.jpg')
flip1_img1=img1.transpose(Image.FLIP_LEFT_RIGHT)
flip2_img1=img1.transpose(Image.FLIP_TOP_BOTTOM)
flip1_img1.show()
flip2_img1.show()
Rot90_img=img.transpose(Image.ROTATE_90)
Rot180_img=img.transpose(Image.ROTATE_180)
Rot270_img=img.transpose(Image.ROTATE_270)
img.show()
Rot90_img.show()
Rot180_img.show()
Rot270_img.show()