import os
from box.exceptions import BoxvalueError
from textSummarizer.logging import logger
import yaml
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """read_yaml file and return
    
    Args: 
        path_to_yaml (str): Path like input

    Raises:
        ValueError: If yaml file is empty
        e: empty yaml file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except  BoxvalueError:
        raise ValueError("yaml file is empty")
    

    except Exception as e:
        raise e
    



@ensure_annotations
def create_directory(path_to_directory: list, verbose=True):
    """
    Creates directories if they don't exist.
    
    Args:
        path_to_directory (list): List of paths to directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directory:
        os.makedirs(path, exist_ok=True)

        if verbose:
            logger.info(f"Created Directory at : {path}")



@ensure_annotations
def get_file_size(path: Path) -> str:
    """
    Get Size in KB

    Args:
        path (Path): Path of file

    Returns:
        str: Size in KB
    """

    size_in_KB = round(os.path.getsize(path)/1024)
    return f"{size_in_KB} KB"