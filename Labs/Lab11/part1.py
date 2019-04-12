from __future__ import absolute_import, division, print_function

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import PIL.ImageOps

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0

test_images = test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)

predictions = model.predict(test_images)

predictions[0]

np.argmax(predictions[0])

test_labels[0]

def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  
  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'
  
  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1]) 
  predicted_label = np.argmax(predictions_array)
 
  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

# Plot the first X test images, their predicted label, and the true label
# Color correct predictions in blue, incorrect predictions in red
#num_rows = 5
#num_cols = 3
#num_images = num_rows*num_cols
#plt.figure(figsize=(2*2*num_cols, 2*num_rows))
#for i in range(num_images):
#  plt.subplot(num_rows, 2*num_cols, 2*i+1)
#  plot_image(i, predictions, test_labels, test_images)
#  plt.subplot(num_rows, 2*num_cols, 2*i+2)
#  plot_value_array(i, predictions, test_labels)
#plt.show()

# Plot the first X test images, their predicted label, and the true label
# Color correct predictions in blue, incorrect predictions in red


#num_rows = 5
#num_cols = 3
#num_images = num_rows*num_cols
#plt.figure(figsize=(2*2*num_cols, 2*num_rows))
#for i in range(num_images):
# plt.subplot(num_rows, 2*num_cols, 2*i+1)
#  plot_image(i+9000, predictions, test_labels, test_images)
# plt.subplot(num_rows, 2*num_cols, 2*i+2)
#  plot_value_array(i+9000, predictions, test_labels)
#plt.show()

shirt = Image.open("Plain+T-Shirt.jpg")
pants = Image.open("pants.jpg")
sandal = Image.open("sandal.jpg")

shirt = shirt.resize((28,28))
pants = pants.resize((28,28))
sandal = sandal.resize((28,28))

shirt = shirt.convert('L')
pants = pants.convert('L')
sandal = sandal.convert('L')

shirt = PIL.ImageOps.invert(shirt)
pants = PIL.ImageOps.invert(pants)
sandal = PIL.ImageOps.invert(sandal)

shirt.save("greyscaleShirt.jpg")
pants.save("greyscalePants.jpg")
sandal.save("greyscaleSandal.jpg")

shirt = np.array(shirt)
pants = np.array(pants)
sandal = np.array(sandal)

shirt = shirt/255.0
pants = pants/255.0
sandal = sandal/255.0

shirt = (np.expand_dims(shirt,0))
pants = (np.expand_dims(pants,0))
sandal = (np.expand_dims(sandal,0))


#shirt prediction
prediciton_shirt = model.predict(shirt)
typeShirt = np.argmax(prediciton_shirt[0])
print(prediciton_shirt)

print(typeShirt)
print(class_names[typeShirt])

plot_value_array(0, prediciton_shirt, test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)
plt.show()

#pants prediciton
predicition_pants = model.predict(pants)
print(predicition_pants)
typePants = np.argmax(predicition_pants[0])

print(typePants)
print(class_names[typePants])

plot_value_array(0, predicition_pants, test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)
plt.show()

#sandal prediction
prediciton_sandal = model.predict(sandal)
print(prediciton_sandal)

typeSandal = np.argmax(prediciton_sandal[0])

print(typeSandal)
print(class_names[typeSandal])

plot_value_array(0, prediciton_sandal, test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)
plt.show()
