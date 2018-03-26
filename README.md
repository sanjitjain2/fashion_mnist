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

Layer (type)

=================================================================

conv2d_1 (Conv2D)            (None, 28, 28, 32)

max_pooling2d_1 (MaxPooling2 (None, 14, 14, 32)

conv2d_2 (Conv2D)            (None, 14, 14, 64)

max_pooling2d_2 (MaxPooling2 (None, 7, 7, 64)  

flatten_1 (Flatten)          (None, 3136)              

dense_1 (Dense)              (None, 1024)              

dropout_1 (Dropout)          (None, 1024)              

dense_2 (Dense)              (None, 10)                

=================================================================
Total params: 3,274,634     

Trainable params: 3,274,634     

Non-trainable params: 0
