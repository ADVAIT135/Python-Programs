from matplotlib import pyplot as plt
import numpy as np
cars=['INSTAGRAM','FACEBOOK','TWITTER','SNAPCHAT','LINKEDIN','REDDIT']
data=[27,41,15,29,18,16]
fig=plt.figure(figsize=(10,7))
plt.pie(data,labels = cars)
plt.show()