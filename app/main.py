from typing import Union
import os
import pickle
from enum import Enum

from fastapi import FastAPI

app = FastAPI()


class SecurityName(str, Enum):
    etfs = 'etfs'
    stock = 'stock'


@app.get("/predict")
def predict(
    vol_moving_avg: float,
    adj_close_rolling_med: float,
    security: Union[SecurityName, None] = None
):
    """
    Predicts ETFs and Stock volume based on the volume moving average
    and adjusted closing rolling median 

    Args:
        vol_moving_avg (float): The moving average volume of the combined security
        adj_close_rolling_med (float): The adjusted closing rolling median 
        security (SecurityName): The name of a specific security: either stock or etfs

    Returns:
        float: The predicted volume
    """

    print("Input: moving average is %s and adjusted closing rolling median is %s ",
          vol_moving_avg, adj_close_rolling_med)

    model_path = ''
    if security is SecurityName.etfs:
        model_path = os.getcwd() + '/app/model/etfs_model'
    elif security is SecurityName.stock:
        model_path = os.getcwd() + '/app/model/stock_model'
    else:
        model_path = os.getcwd() + '/app/model/combine_model'

    input_value = [[vol_moving_avg, adj_close_rolling_med]]

    model = ''
    # Load the model from the disk
    print("Load the trained model from the disk")
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
    except Exception as e:
        error_message = "Input Error, please enter the correct data type: float or integer"
        print(error_message)
        print(e)
        return {'error_message': error_message}

    # Predict the volume
    print("Predict the security volume")
    value = model.predict(input_value)
    print("The predicted value is %s", value)
    print(value)
    return {'predicted_volume': value[0]}
