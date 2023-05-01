import tensorflow as tf
mnist = tf.keras.datasets.mnist

(X, YT), (x, yt) = mnist.load_data()

X, x = X/255, x/255
X, x = X.reshape((60000,784)), x.reshape((10000,784))

model = tf.keras.models.load_model("model.h5")

y=model.predict(x)
print(y[0])
import numpy as np
print(np.argmax(y[0]), yt[0])

import matplotlib.pyplot as plt
x=x.reshape(10000,28,28)
plt.imshow(x[0])
plt.show()
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(x[i], cmap=plt.cm.binary)
    plt.xlabel(np.argmax(y[i]))
plt.show()
               
