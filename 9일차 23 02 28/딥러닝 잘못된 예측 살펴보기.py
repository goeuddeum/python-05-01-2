import tensorflow as tf
mnist = tf.keras.datasets.mnist

(X, YT), (x, yt) = mnist.load_data()

X, x = X/255, x/255
X, x = X.reshape((60000,784)), x.reshape((10000,784))

model = tf.keras.models.load_model("model.h5")

y=model.predict(x)

import numpy as np
import matplotlib.pyplot as plt
x=x.reshape(10000,28,28)
cnt_wrong=0
y_wrong=[]
for i in range(10000):
    if np.argmax(y[i]) !=yt[i]:
        y_wrong.append(i)
        cnt_wrong += 1
print(cnt_wrong)
print(y_wrong[:10])
