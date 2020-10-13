from PIL import Image
import os
size_100=(100,100)
size_200=(200,200)
size_300=(300,300)
size_400=(400,400)
size_500=(500,500)
size_600=(600,600)
size_700=(700,700)
for f in os.listdir('.'):
    if f.endswith(('.jpg','.png')):
        i=Image.open(f)
        fn,fext=os.path.splitext(f)
        
        i.thumbnail(size_700)
        i.save('700x700/{}_700{}'.format(fn,fext))
        
        i.thumbnail(size_600)
        i.save('600x600/{}_600{}'.format(fn,fext))
        
        i.thumbnail(size_500)
        i.save('500x500/{}_500{}'.format(fn,fext))
        
        i.thumbnail(size_400)
        i.save('400x400/{}_400{}'.format(fn,fext))
        
        i.thumbnail(size_300)
        i.save('300x300/{}_300{}'.format(fn,fext))
        
        i.thumbnail(size_200)
        i.save('200x200/{}_200{}'.format(fn,fext))
        
        i.thumbnail(size_100)
        i.save('100x100/{}_100{}'.format(fn,fext))