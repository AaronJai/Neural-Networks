# We will build a feedforward neural network and train it to solve a real problem with Keras

### A classic machine learning problem:
MNIST handwritten digit classifcation - given an image, classify it as a digit.

**Keras is a powerful deep learning library for python.**

Each image in the MNIST dataset is 28x28 and contains a centered, grayscale digit. We’ll flatten each 28x28 into a 784 dimensional vector, which we’ll use as input to our neural network. Our output will be one of 10 possible classes: one for each digit.

### Setup
> pip install tensorflow numpy mnist
No need to install keras package as it is bundled with TensorFlow

### ISSUE
There is an issue with imports where it 'cannot be resolved'

>from tensorflow.keras.models import Sequential
>from tensorflow.keras.layers import Dense
>from tensorflow.keras.utils import to_categorical

**nor**

>from tensorflow import keras
>rom keras.models import Sequential
>from keras.layers import Dense
>rom keras.utils import to_categorical

works..

Inspiration: [Victor Chou](https://victorzhou.com/blog/keras-neural-network-tutorial/)