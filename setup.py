from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = [req.replace("\n", "") for req in file_obj.readlines()]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='Suraj Varma',
    author_email='surajvarma823@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=get_requirements('requirements.txt'),
)
