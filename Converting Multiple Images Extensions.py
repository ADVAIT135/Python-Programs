from PIL import Image
import os
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i=Image.open(f)
        fn,fext=os.path.splitext(f)
        i.save('pngim/{}.png'.format(fn))