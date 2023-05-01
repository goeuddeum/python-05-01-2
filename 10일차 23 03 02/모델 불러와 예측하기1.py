import tensorflow as tf
from _8seg_data import X,YT

model=tf.keras.models.load_model("model.h6")
Y=model.predict(X)
print(Y)