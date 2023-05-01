import numpy as np
X=np.random.randint(0,256,(3,3,1))

import matplotlib.pyplot as plt
plt.imshow(X)
plt.show()
print(X[0:3,0:3,0])

F=np.random.randint(0,256,(3,3,1))
plt.imshow(F)
plt.show()
print(F[:,:,0])

plt.imshow(X*F)
plt.show()
print((X*F)[:,:,0])
print(np.sum(X*F))