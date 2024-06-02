import os
import yaml
from pathlib import Path
from src.logger import logging
from src.exception import CustomeException
from typing import Any
import base64
from ensure import ensure_annotations
import json
import joblib
import sys
from box import ConfigBox
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(file_path:Path)->ConfigBox:
    """This function is used to read yaml file"""

    try:
        with open(file_path) as file_obj:
            content = yaml.safe_load(file_obj)
            logging.info(f"{file_path} ymal file load Successfully !")
        
        return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise CustomeException(e,sys)

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    
    """This function is used to create directories"""
    
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)

        if verbose:
            logging.info(f"Create directories at : {path}")

    
@ensure_annotations
def save_json(file_path:Path,data:dict):
    """This function is used to save json data"""

    try:
        with open(file_path,'w') as file_obj:
            json.dump(data,file_obj,indent=4)
            logging.info(f"Json file {file_path} save successfully")

    except Exception as e:
        raise CustomeException(e,sys)
    

@ensure_annotations
def load_json(file_path:Path)->ConfigBox:
    """This function is used to load json data"""

    try:
        with open(file_path) as file_obj:
            data = json.loads(file_obj)
            logging.info(f"Load json file {file_path} successfully")

            return ConfigBox(data)
    
    except Exception as e:
        raise CustomeException(e,sys)

@ensure_annotations
def save_bin(file_path:Path,data:Any)->Any:
    """This function is used to save binary file"""

    try:
        joblib.dump(data,file_path)
    except Exception as e:
        raise CustomeException(e,sys)

@ensure_annotations
def load_bin(file_path:Path):
    """This function is used to load binary file"""

    try:
        data = joblib.load(file_path)
        logging.info(f"binary file {file_path} successfully load")

        return data
    except Exception as e:
        raise CustomeException(e,sys)

@ensure_annotations
def get_size(filename:Path)->str:
    """This function is used to get the size of the file"""

    try:
        size = os.path.getsize(filename=filename)
        return size
    
    except Exception as e:
        raise CustomeException(e,sys)

@ensure_annotations
def decode_image(imageString:str,filename:Path):
    """This function is used to decode the image """

    imageData = base64.b64decode(imageString)

    with open(filename,'wb') as file_obj:
        file_obj.write(imageData)
        file_obj.close()


@ensure_annotations
def encode_image(cropImagePath:Path):
    """This function is used to encode the image """

    with open(cropImagePath,'rb') as file_obj:
        return base64.b64encode(file_obj.read())

