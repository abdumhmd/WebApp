import tensorflow as tf
import numpy as np
from keras.preprocessing import image
model = tf.keras.models.load_model('model/model.h5')
def pred(data):
    emotions = {0:'Angry', 1:'Disgust', 2:'Fear', 3:'Happy', 4:'Sad', 5:'Surprise', 6:'Neutral'}
    img=image.load_img(data, target_size=(197, 197,3))
  
    x=image.img_to_array(img)
    x=x/255.
    x=np.expand_dims(x, axis=0)
    images = np.vstack([x])
    
    classes = model.predict(images)
    
    
    # You may want to further format the prediction to make it more
    # human readable
    print(emotions.get(np.argmax(classes[0])))
    return emotions.get(np.argmax(classes[0]))