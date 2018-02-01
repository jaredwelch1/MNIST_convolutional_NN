# MNIST Convolutional NN

Using the standard MNIST dataset for written digits, this is a notebook exploration and implementation of a Convolutional Neural Network. 

## To Do

- experiement with feature sizes from convolutional layers. (right now has 32, 64) 
- try a new CNN using colors. Currently using an input of pictures * grayscale value on MNIST.
	- right now the small patches are 5*5*1, but with many CNNs they use red, green, yellow color values rather than
	grayscale, so when trying with real images keep that in mind

### Structure:

- Images [28 * 28]

- 2 convolutional layers that use pooling in between

	- layer 1: convolution of 5x5 into 32 feature maps of 24*24 (no padding and strive of 1)
	- pooling to reduce from 28x28 to 14x14

	- layer 2: convolution of 5x5 into 64 feature maps
	- pooling to reduce to 7x7

- next fully activated layer 
- dropout
- output softmax 

