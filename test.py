import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


tf.set_random_seed(0)
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
