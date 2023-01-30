import os
import pickle
import pandas as pd
import numpy as np
import joblib

from google.cloud.aiplatform.prediction.predictor import Predictor
from google.cloud.aiplatform.utils import prediction_utils

class MyPredictor(Predictor):
    """An example Predictor for an AI Platform custom prediction routine."""

    def __init__(self):
        """Stores artifacts for prediction. Only initialized via `from_path`.
        """
        return

    def load(self, artifacts_uri: str):
        prediction_utils.download_model_artifacts(artifacts_uri)
        self._model = joblib.load("model.pkl")
    
    def predict(self, instances):
        """Performs custom prediction.
        Preprocesses inputs, then performs prediction using the trained
        scikit-learn model.
        Args:
            instances: A list of prediction input instances.
        Returns:
            A list of outputs containing the prediction results.
        """
        instances = instances['instances']
        inputs = np.asarray(instances)
        data = pd.DataFrame(inputs)
        outputs = self._model.transform(data)
        return {"predictions": outputs.tolist()}
