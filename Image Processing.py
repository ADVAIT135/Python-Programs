from PIL import Image
img=Image.open('ADU.jpg')
print(img.size)
print(img.format)
img.show()