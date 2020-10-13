from PIL import Image
img=Image.open('ADU.jpg')
area=(0,0,500,500)
crop_img=img.crop(area)
img.show()
crop_img.show()
