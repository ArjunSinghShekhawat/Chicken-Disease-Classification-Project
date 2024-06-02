import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.losses import CategoricalCrossentropy
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load model with custom deserialization for CategoricalCrossentropy
        custom_objects = {'CategoricalCrossentropy': CategoricalCrossentropy}
        model = load_model(os.path.join("artifacts", "training", "model.h5"), custom_objects=custom_objects)

        # Load and preprocess the image
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # Predict the class of the image
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        # Interpret the result
        if result[0] == 1:
            prediction = 'Healthy'
        else:
            prediction = 'Coccidiosis'
        
        return [{"image": prediction}]
