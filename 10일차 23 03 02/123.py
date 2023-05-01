import tensorflow as tf
#mnist=tf.keras.datasets.fashion_mnist
mnist=tf.keras.datasets.cifar100
(X,YT),(x,yt) = mnist.load_data()

print(X.shape,YT.shape,x.shape,yt.shape)

import matplotlib.pyplot as plt
plt.imshow(X[0])
#plt.show()

print(YT[0])
print(max(YT))
#print(tf.one_hot(YT[0],100))

#for row in range(28):
#    for col in range(28):
#        print('%4s' %X[0][row][col],end='')
#        print()

#plt.figure(figsize=(10,10))
#for i in range(100):
#    plt.subplot(20,5,i+1)
#    plt.xticks([])
#    plt.yticks([])
#    plt.imshow(X[i])
#    plt.xlabel(YT[i])
#plt.show()
X,x=X/255,x/255
X,x=X.reshape,((60000,28*28)),x.reshape((10000,28*28))
model=tf.keras.Sequential([
    tf.keras.Input(shape=(28*28,)),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dense(10,activation='sotfmax')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentroppy',
              metrics=['accuracy'])
model.fit(X,YT,epochs=5)
model.evaluate(x,yt)