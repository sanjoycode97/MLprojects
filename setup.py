from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements from the provided file path.
    It removes any extra blank lines or the '-e .' entry.
    """
    requirements = []
    with open(file_path) as file_obj:
        # Read all lines from the file, strip extra spaces/newlines
        requirements = [req.strip() for req in file_obj.readlines() if req.strip()]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='MLprojects',
    version='0.0.1',
    author='sanjoy',
    author_email='sanjoy.sarkar.work@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
