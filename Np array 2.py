import numpy as np
a=np.array(([1,2,3,4],[5,6,7,8],[8,9,10,11,12]))
print(a)
b=a[:2,1:3]
print(b)
print(a[0,1])
b[0,0]=75
print(a[0,1])
print(a)