# MNIST Convolutional NN

Using the standard MNIST dataset for written digits, this is a notebook exploration and implementation of a Convolutional Neural Network. 

### Structure:

- Images [28 * 28]

- 2 convolutional layers that use pooling in between

	- layer 1: convolution of 5x5 into 32 features
	- reshape into original dimension
	- pooling to reduce from 28x28 to 14x14

	- layer 2: convolution of 5x5 into 64 features
	- reshape
	- pooling to reduce to 7x7

- next fully activated layer 
- dropout
- output softmax 

