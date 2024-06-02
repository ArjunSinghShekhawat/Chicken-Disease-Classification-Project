import os
from pathlib import Path
import logging

<<<<<<< HEAD
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

file_list = [
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/pipeline/__init__.py",
    f"src/config/__init__.py",
    f"src/config/configuration.py",
    f"src/entity/__init__.py",
    f"src/constants/__init__.py",
    f"src/utils/__init__.py",
    f"src/exception.py",
    f"src/logger.py",
    f"params.yaml",
    f"requirements.txt",
    f"main.py",
    f"setup.py",
    f"README.md",
    f".gitignore",
    f"templates/index.html",
    f"templates/home.html"
]

for file_path in file_list:
    file_path = Path(file_path)
    filedir,filename = os.path.split(file_path)


    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info("Directory Successfully Created !")
    
    if (not os.path.exists(filename)) or (os.path.getsize(filename)==0):
        with open(filename,'w') as file_obj:
            pass
        logging.info("File Successfully Create !")
    else:
        logging.info(f"{filename} is already exists !")
=======
logging.basicConfig(
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

list_of_files = [
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/utils/__init__.py",
    f"src/config/__init__.py",
    f"src/config/configuration.py",
    f"src/pipeline/__init__.py",
    f"src/entity/__init__.py",
    f"src/constants/__init__.py",
    f"templates/index.html",
    f"templates/home.html",
    f"README.md",
    f".gitignore",
    f"requirements.txt",
    f"setup.py",
    f"params.yaml"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir,file_name = os.path.split(file_path)

    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,'w') as file_obj:
            pass
        logging.info("File created {}".format(file_name))
    else:
        logging.info("File allready exists {}".format(file_name))
        



>>>>>>> 03dd003 (first commit)
