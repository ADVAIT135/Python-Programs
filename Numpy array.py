import numpy as np
a=np.array([1,2,3])
print(a)
print(a.shape)
print(a[0],a[1],a[2])
a[0]=5
print(a)
b=np.array(([1,2,3],[4,5,6]))
print(b)
print(b.shape)
print(b[0,0])
c=np.array([1.0,2.1,3.4])
print(c)
a=np.zeros((2,3))
print(a)
b=np.ones((1,2))
print(b)
c=np.full((2,3),7)
print(c)
e=np.random.random((3,3))
print(e)