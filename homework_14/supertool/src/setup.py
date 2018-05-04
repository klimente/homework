# Licence MIT

import os
from setuptools import setup, find_packages
import supertool.files_handler

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
    name='supertool-distro',
    version='0.1',
    description='Super-super tool to inspect directory for similar files',
    author='Klimenko Andrey',
    author_email='zaktoq@gmail.com',
    license='MIT',
    classifiers=[
        'Topic :: Education',
        'Programming Language :: Python :: 3.6',

    ],
    packages=find_packages(exclude=['tests'],include=['supertool']),
    install_requires=extract_requirments(os.path.join(DISTRO_ROOT_PATH,'requirements','base.txt')),
    test_requires=extract_requirments(os.path.join(DISTRO_ROOT_PATH,'requirements','test.txt')),
    test_suite='nose.collector',
    scripts=[os.path.join('bin','similar_files')],
    zip_safe=False

)
