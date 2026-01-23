# Utility -> functionality used frequently across the project
import os
from box.exceptions import BoxValueError
import yaml
from ChestCancerClassifer import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path 
from typing import Any 
import base64 


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns 
    
    Args:
        path_to_yaml (str): Path to the yaml file.

    Raises:
        ValueError: If the file is empty.
    
    Returns:
        ConfigBox: The loaded configuration.
    """
    try:
        print(f"Reading yaml file : {path_to_yaml}")
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def save_json(path: Path, data: dict):
    """ Saves json data to a file.
    
    Args:
        path (Path): path to json file 
        data (dict): data to be saved in json file  
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info("JSON file saved at: {path}")

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    
    """
    for path in path_to_directories:
        os.makedir(path, exist_ok = True)
        if verbose:
            logger.info(f"created directory at : {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """ load json files data 

    Args:
        path (Path): path to json file
    
    Returns:
        ConfigBox: data as class attributes instead of dict 
    
    """
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """ save binary file
    
    Args:
        data (any): data to be saved as binary 
        path (Path): path to binary file 
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """ load binary data 
    
    Args: 
        path (Path): path to binary file 

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data 

@ensure_annotations
def get_size(path: Path) -> str:
    """ get size in KB 
    
    Args:
        path (path): path of the file 
    
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

def decodeImage(imgString, fileName):
    imgdata = base64.b64decode(imgString)
    with open(fileName, "wb") as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())