from setuptools import setup,find_packages
from typing import List


HYPEN_E_DOT = "-e ."
def get_requirements(file_path: str) -> List[str]:
    """This method is used to find all required packages"""

    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()

        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    author="Arjun Singh Shekhawat",
    author_email="shekhawatsingharjun12345@gmail.com",
    name="Chicken Disease Classification",
    version="0.0.1",
    description='End to End deep learning projects with using pipeline concept and industry standard project structure of this project. In this project used python, pandas, numpy, tensorflow, seaborn, matplotlib, Flask and more library and packages are used in this project. This project is industry standard project.',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)
