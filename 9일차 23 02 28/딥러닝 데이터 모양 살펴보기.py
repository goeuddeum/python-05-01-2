import tensorflow as tf
mnist = tf.keras.datasets.mnist
(X, YT), (x, yt) = mnist.load_data()
print(X.shape, YT.shape, x.shape, yt.shape)