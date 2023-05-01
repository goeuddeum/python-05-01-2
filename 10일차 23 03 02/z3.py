import tensorflow as tf
from _8seg_data import X,YT_1
model=tf.keras.Sequential([
    tf.keras.Input(shape=(7,)),
    tf.keras.layers.Dense(16,activation='relu'),
    tf.keras.layers.Dense(1,activation='linear')
])
model.compile(optimizer='adam',loss='mse')
model.fit(X,YT_1,epochs=10000)
Y=model.predict(X)
print(Y)
