import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img)
    pil_img = Image.fromarry(np.uint8)
    pil_img.show()

(x_train,t_train),(x_test,y_test) = losd.mnidt(flstten=True,normalize=False)

img = x_train[0]
label = t_train[0]
print(label)

print(img.shape)
img = img.reshape(28, 28)
print(img.shape)

img_show(img)
