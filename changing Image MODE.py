from PIL import Image
img=Image.open('Python.png')
new_img=img.convert("RGB")
#for black and white image Type "L" instead of "RGB"
new_img.show()


