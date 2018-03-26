import sys
import argparse
import numpy as np
from PIL import Image 
import requests
from io import BytesIO
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

from keras.models import load_model
from keras.preprocessing import image

label_dict = {
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
}

target_size = (28,28)
model = load_model('fashion_mnist_2.h5')

def predict(model, img, target_size, top_n=1):
    if img.size != target_size:
        temp = img.resize(target_size)
        temp.save('check1.jpg')
    x = image.img_to_array(temp)
    x = np.expand_dims(x, axis=0)
    preds = model.predict(x)
    output_label = [np.where(r==1)[0] for r in preds]
    return int(output_label[0])
    


if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--image", help="path to image")
    a.add_argument("--image_url", help="url to image")
    args = a.parse_args()

    if args.image is None and args.image_url is None:
        a.print_help()
        sys.exit(1)

    if args.image is not None:
        img = Image.open(args.image).convert('L')
        label = predict(model, img, target_size)
        print label_dict[label]