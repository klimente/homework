#License MIT
import os
from setuptools import setup, find_packages

DISTRO_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

def extract_requirments(file):
    """
    Extract requirements from requirements file

    :param file: path requirements file
    :type file: str
    :return: list[str] -- list of requirements
    """
    with open(file,'r') as file:
        return file.read().splitlines()

setup(
    name='stats-distro',
    version='0.1',
    description='Modul for working with data',
    author='Klimenko Andrey',
    author_email='zaktoq@gmail.com',
    license='MIT',
    classifiers=[
        'Topic :: Education',
        'Programming Language :: Python :: 3.6',

    ],
    packages=find_packages(exclude=['tests', 'example'],include=['stats']),
    install_requires=extract_requirments(os.path.join(DISTRO_ROOT_PATH,'requirements', 'base.txt')),
    test_requires=extract_requirments(os.path.join(DISTRO_ROOT_PATH,'requirements', 'test.txt')),
    test_suite='nose.collector',
)