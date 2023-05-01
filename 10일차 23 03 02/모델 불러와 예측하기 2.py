import tensorflow as tf
from _8seg_data import X
model=tf.keras.models.load_model("model.h6")
x=X[:1]
print(x.shape)
Y=model.predict(X)
print(Y)