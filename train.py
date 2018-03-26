import keras
from keras.layers import Conv2D, MaxPool2D, Flatten
from keras.layers import Dense, Dropout
from keras.models import Sequential
import mnist_reader

def create_model():

    model = Sequential()
    model.add(Conv2D(32,(5,5),padding="same",input_shape=[28,28,1]))
    model.add(MaxPool2D((2,2)))
    model.add(Conv2D(64,(5,5),padding="same"))
    model.add(MaxPool2D((2,2)))
    model.add(Flatten())
    model.add(Dense(1024,activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10,activation='softmax'))
    model.compile(keras.optimizers.Adam(1e-4), loss='categorical_crossentropy',
                     metrics=['accuracy'])
    return model


X_train, y_train = mnist_reader.load_mnist('data',kind='train')
X_test, y_test   = mnist_reader.load_mnist('data',kind='t10k')

print(y_test.shape)

X_train = X_train.reshape([-1, 28, 28, 1])
X_test = X_test.reshape([-1, 28, 28, 1])
X_train = X_train/255
X_test = X_test/255
y_train = keras.utils.np_utils.to_categorical(y_train)
y_test = keras.utils.np_utils.to_categorical(y_test)

model = create_model()
model.summary()
model.fit(X_train,y_train,validation_split=0.10,
            batch_size=64,epochs=25,verbose=2)

model.save('/output/fashion_mnist_2.h5')
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=2)
