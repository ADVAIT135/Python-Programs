from PIL import Image
img=Image.open('ADU.jpg')
img.save('ADU.png')
img1=Image.open('Python.png')
new_img1=img1.convert("RGB")
new_img1.save('Python.jpg')