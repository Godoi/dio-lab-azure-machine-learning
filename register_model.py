import json
import numpy as np
from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path('diabetes-regression-model')
    model = joblib.load(model_path)

def run(raw_data):
    try:
        data = json.loads(raw_data)
        data = np.array(data['data'])
        result = model.predict(data)
        return result.tolist()
    except Exception as e:
        error = str(e)
        return error
