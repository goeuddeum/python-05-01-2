import tensorflow as tf
import numpy as np

X=np.array([[2]])
YT=np.array([[10]])
W=np.array([[3]])
B=np.array([1])

model=tf.keras.Sequential([
    tf.keras.Input(shape=(1,)),
    tf.keras.layers.Dense(1)
    ])
model.layers[0].set_weights([W,B])
model.compile(loss='mse',optimizer='sgd')
Y=model.predict(X)
print(Y)

model.fit(X,YT,epochs=1000)
print('W=',model.layers[0].get_weights()[0])
print('B=',model.layers[0].get_weights()[1])
Y=model.predict(X)
print(Y)