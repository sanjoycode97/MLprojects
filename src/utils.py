import os
import sys
import pickle
import numpy as np
import pandas as pd
from src.exception import CustomException

def save_object(file_path, obj):
    """
    Saves a Python object to the specified file path using pickle.

    Args:
        file_path (str): The path where the object should be saved.
        obj (Any): The Python object to serialize and save.

    Raises:
        CustomException: If saving fails due to an exception.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
