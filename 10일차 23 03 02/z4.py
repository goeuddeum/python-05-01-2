import tensorflow as tf
from _8seg_data import X,YT
X,YT=YT,X
model=tf.keras.Sequential([
    tf.keras.Input(shape=(4)),
    tf.keras.layers.Dense(16,activation='relu'),
    tf.keras.layers.Dense(7,activation='linear')
])
model.compile(optimizer='adam',loss='mse')
model.fit(X,YT,epochs=10000)
Y=model.predict(X)
print(Y)