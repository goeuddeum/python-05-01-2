import numpy as np
np.set_printoptions(precision=2,suppress=True)

X=np.random.randint(0,256,(60000,32,32,3))
YT=np.random.randint(0,1000,(60000,))
import matplotlib.pyplot as plt
print(YT[0])
plt.imshow(X[0])
#plt.show()

X=X/255
X=X.reshape(60000,32*32*3)
import tensorflow as tf
model=tf.keras.Sequential([
    tf.keras.Input(shape=(32*32*3,)),
    tf.keras.layers.Dense(512,activation='relu'),
#    tf.keras.layers.Dense(10,activation='relu'),
    tf.keras.layers.Dense(1000,activation='softmax')
])
model.compile(optimizer='Adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(X,YT,epochs=10)
#Y=model.predict(X)
#print(YT)
#print(Y)

