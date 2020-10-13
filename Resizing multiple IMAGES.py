from PIL import Image
import os
size_200=(200,200)
for f in os.listdir('.'):
    if f.endswith(('.jpg','.png')):
        i=Image.open(f)
        fn,fext=os.path.splitext(f)
        i.thumbnail(size_200)
        i.save('jpgim/{}_200{}'.format(fn,fext))