import os
import pickle

import numpy as np
import joblib
import pandas as pd

from google.cloud.aiplatform.prediction.predictor import Predictor
from google.cloud.aiplatform.utils import prediction_utils


class MyPredictor(Predictor):
    """An example Predictor for an AI Platform custom prediction routine."""

    def __init__(self):
        return
        """Stores artifacts for prediction. Only initialized via `from_path`.
        """
        
    def load(self, artifacts_uri: str):
        prediction_utils.download_model_artifacts(artifacts_uri)
        
        self._column_names = ['PassengerId', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
        self._model = joblib.load("model.pkl")

    def predict(self, instances):
        """Performs custom prediction.
        Preprocesses inputs, then performs prediction using the trained
        scikit-learn model.
        Args:
            instances: dictionary with key 'instances' that has a list of prediction input instances.
        Returns:
            a dictionary with key 'predictions' and values as a list of outputs containing the prediction results.
        """
        print('1',type(instances), instances)
        instances = instances['instances']
        print('2',type(instances), instances)
        inputs = np.asarray(instances)
        print('3', type(inputs), inputs)
        data = pd.DataFrame(inputs, columns=self._column_names)
        outputs = self._model.transform(data)
        return {"predictions": outputs.tolist()}
