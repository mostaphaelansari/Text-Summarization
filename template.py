import os
from pathlib import Path
import logging

# Correct logging configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Project name
project_name = 'testSummarizer'

# List of files and directories to be created
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

# Create the directories and files if they don't exist
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Directory created: {filedir} for the file {filepath}")
    
    if not filepath.exists():
        with open(filepath, 'w') as f:
            pass  # Create an empty file
        logging.info(f"File created: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")

if __name__ == "__main__":
    print("Template script is running...")