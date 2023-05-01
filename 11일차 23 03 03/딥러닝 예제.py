import tensorflow as tf
import numpy as np



X,x=X/255,x/255
X,x=X.reshape((50000,3072)),x.reshape((10000,3072))

model=tf.keras.Sequential([
    tf.keras.Input(shape=(3072,)),
    tf.keras.layers.Dense(1024,activation='relu'),
    tf.keras.layers.Dense(100,activation='softmax')
])

model.compile(optimizer='adam',loss='categorical_crossentropy',
              metrics=['accuracy'])

amodel.fit(X,YT,epochs=5)

model.evaluate(X,YT)