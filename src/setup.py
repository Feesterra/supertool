# License MIT

import os
from setuptools import setup, find_packages


DISTRO_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


def extract_requirements(file):
    """
    Extracts requirements from requirements file

    :param file: path to requirements file
    :type file: str
    :return: list[str] -- list of requirements
    """

    with open(file, 'r') as file:
        return file.read().splitlines()

setup(
    name='supertool-distro',
    version='0.1',
    description='super-super tool. Instruments: similar files (gui is called by ''gui_similar.py'' command, '
                'weather (gui is called by ''weather_gui.py'' command, calculator with ''python window.py'' command',
    author='Ich',
    author_email='elena@gmail.com',
    license='MIT',
    classifiers=[
        'Topic :: Education',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=extract_requirements(os.path.join(DISTRO_ROOT_PATH, 'requirements', 'base.txt')),
    test_requires = extract_requirements(os.path.join(DISTRO_ROOT_PATH, 'requirements', 'test.txt')),
    test_suite='nose.collector',
    scripts=[os.path.join('bin', 'similar_files'), os.path.join('bin', 'weather_forecast'),
             os.path.join('supertool', 'gui_similar.py'), os.path.join('supertool', 'weather_gui.py')]

)
