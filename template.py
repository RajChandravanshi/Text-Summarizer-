import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"    
]

for filepath in list_of_files:
    filepath = Path(filepath)  # Correct usage of Path
    filedir = filepath.parent  # Get the directory path
    filename = filepath.name   # Get the file name

    if filedir != "":
        filedir.mkdir(parents=True, exist_ok=True)  # Create directory if it doesn't exist
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()  # Create the file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")
