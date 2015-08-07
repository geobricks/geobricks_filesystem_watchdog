from setuptools import setup
from setuptools import find_packages

setup(
    name='GeobricksFilesystemWatchdog',
    version='0.0.1',
    author='Simone Murzilli; Guido Barbaglia',
    author_email='geobrickspy@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    description='Geobricks File System watchdog library.',
    install_requires=[
        # 'watchdog',
        # 'flask',
        # 'flask-cors',
        # 'requests'
    ],
    url='http://pypi.python.org/pypi/GeobricksFilesystemWatchdog/',
    keywords=['geobricks', 'filesystem', 'watchdog']
)
