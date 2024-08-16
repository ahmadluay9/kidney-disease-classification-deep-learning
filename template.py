# Import Library
import os
from pathlib import Path
import logging

# Logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Project name
project_name = 'cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep", # This is a hidden file commonly used in Git repositories to keep an empty directory from being deleted.
    
    # use f-strings to dynamically create filenames. These filenames follow a specific structure
    # Each subdirectory has an __init__.py file, which is a convention in Python to treat the directory as a package.
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    
    "config/config.yaml", # a configuration file in YAML format.
    "dvc.yaml", # Data Version Control (DVC).
    "params.yaml", # containing parameters for the project.
    "requirements.txt", #  used to specify dependencies for the project.
    "setup.py", # used for packaging the project using tools like setuptools.
    "research/trials.ipynb", # a Jupyter Notebook file related to research or experimentation within the project.
    "templates/index.html" # This suggests the project might involve web development and may have HTML templates.


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")