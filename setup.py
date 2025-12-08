from setuptools import find_packages, setup
from typing import List

def get_requirement(file_path:str)->List[str]:
    """
    this function returns the list of requirement
    """
    requirement = []
 
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace('\n',"") for req in requirement]

    return requirement



setup(
name='project1',
version=0.001,
author='bhabanti',
author_email='BhabantiPaul2026@u.northwestern.edu',
packages=find_packages(),
install_requires=get_requirement('requirement.txt')
)