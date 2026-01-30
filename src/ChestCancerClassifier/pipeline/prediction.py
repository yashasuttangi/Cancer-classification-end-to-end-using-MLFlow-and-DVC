import numpy as np 
from tensorflow.keras.models import load_model 
from tensorflow.keras.preprocessing import image 
import os 

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load trained model
        model = load_model(os.path.join("model", "model.h5"))

        # Load and preprocess image
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = test_image / 255.0
        test_image = np.expand_dims(test_image, axis=0)

        # Model prediction
        preds = model.predict(test_image)
        class_idx = np.argmax(preds, axis=1)[0]

        CLASS_NAMES = [
            "Adenocarcinoma Cancer",
            "Normal",
            "Squamous Cell Carcinoma"
        ]

        prediction = CLASS_NAMES[class_idx]

        return [{
            "image": prediction,
            "confidence": float(np.max(preds))
        }]
