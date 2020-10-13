from PIL import Image
from PIL import ImageFilter
img=Image.open('ADU.jpg')
img1=Image.open('python.png')
sharp=img.filter(ImageFilter.SHARPEN)
blur=img.filter(ImageFilter.BLUR)
blur.show()
sharp.show()