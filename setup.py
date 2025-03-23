from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlprojects',
    version='0.0.1',
    author='ranjithnathk',
    author_email='ranjithnathk29@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

    

)