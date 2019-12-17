import cv2
import numpy as np
from keras.models import load_model

# Classes
dirs = ['atocha', 'alfonso_xii', 'museo_prado', 'schweppes', 
        'plaza_mayor', 'la_almudena', 'ayuntamiento', 'debod', 
        'puerta_alcala', 'ventas', 'banco_esp', 'jardin_botanico', 'palacio_cristal']

# Loading model
model = load_model('./models/model(0.96).hdf5')

# Predict image
path = '../Local-Final-project/DB.jpeg'
def pred(path):
    im = cv2.imread(path)
    imres1 = cv2.resize(im,(256,256))
    pred = model.predict(np.expand_dims(imres1,axis=0))[0]
    for i, p in enumerate(pred):
        if p > 0.5:
            print(dirs[i], p)

pred(path)