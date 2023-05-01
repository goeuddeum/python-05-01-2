import tensorflow as tf
import numpy as np
X=np.array([[.05,.10]])
YT=np.array([[0.,1.]])
W=np.array([[.15,.25],[.20,.30]])
B=np.array([.35,.35])
W2=np.array([[.40,.50],[.45,.55]])
B2=np.array([.60,.60])
model=tf.keras.Sequential([
    tf.keras.Input(shape=(2,)),
    tf.keras.layers.Dense(2, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')
])
model.layers[0].set_weights([W,B])
model.layers[1].set_weights([W2,B2])
model.compile(optimizer='sgd',
              loss='categorical_crossentropy')
Y=model.predict(X)
print(Y)
model.fit(X,YT,epochs=100000)
print('W=',model.layers[0].get_weights()[0])
print('B=',model.layers[0].get_weights()[1])
print('W2=',model.layers[1].get_weights()[0])
print('b2=',model.layers[1].get_weights()[1])
Y=model.predict(X)
print(Y)