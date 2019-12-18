import cv2
import numpy as np
from keras.models import load_model
import tensorflow as tf
from keras import backend as K

# Classes
dirs = ['Atocha', 'Monumento Alfonso XII', 'Museo Prado', 'Edificio Schweppes', 
        'Plaza Mayor', 'Catedral de La Almudena', 'Ayuntamiento de Madrid', 'Templo de Debod', 
        'Puerta Alcala', 'Plaza de toros Las Ventas', 'Banco España', 'Jardin Botanico', 'Palacio Cristal']

# Loading model
model = load_model('./models/model(0.96).hdf5')

tf_session= K.get_session()
tf_graph = tf.get_default_graph()

# Predict image
#path = '../Local-Final-project/DB.jpeg'
def pred(path):
    im = cv2.imread(path)
    imres = cv2.resize(im,(256,256))
    
    global tf_graph,tf_session
    
    with tf_session.as_default():
            with tf_graph.as_default():

                pred = model.predict(np.expand_dims(imres,axis=0))[0]
                for i, p in enumerate(pred):
                    if p > 0.5:
                        return {
                            "classes":dirs,
                            "prediction":{
                                "label":dirs[i],
                                "prob": str(p)
                            }
                        }

#print(pred(path))