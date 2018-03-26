# fashion_mnist
My attempt on the Fashion-MNIST dataset

Train Accuracy - 96.16%
Validation Accuracy - 92.38% 

# Help
- run   "python test.py --image [PATH_TO_IMAGE]"   to output the class label

# Class Labels for Fashion-MNIST dataset
0: 'T-shirt/top',

1: 'Trouser',

2: 'Pullover',

3: 'Dress',

4: 'Coat',

5: 'Sandal',

6: 'Shirt',

7: 'Sneaker',

8: 'Bag',

9: 'Ankle boot'


# Model Architecture

Layer (type)                 Output Shape              Param #
=================================================================
conv2d_1 (Conv2D)            (None, 28, 28, 32)        832
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 14, 14, 32)        0
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 14, 14, 64)        51264
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 7, 7, 64)          0
_________________________________________________________________
flatten_1 (Flatten)          (None, 3136)              0
_________________________________________________________________
dense_1 (Dense)              (None, 1024)              3212288
_________________________________________________________________
dropout_1 (Dropout)          (None, 1024)              0
_________________________________________________________________
dense_2 (Dense)              (None, 10)                10250
=================================================================
Total params: 3,274,634
Trainable params: 3,274,634
Non-trainable params: 0
