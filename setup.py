from setuptools import setup, find_packages

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='SimpleMySQL',
    version='0.0.1',
    description='A wrapper for MySQL to keep your code free from SQL.',
    long_description='content will follow',
    url='https://github.com/Vozdyx74/SimpleMySQL',
    author='Vozdyx74, HaCsO',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.7'
    ],
    keywords='simple mysql sql database wrapper',
    install_requires=requirements,
    packages=find_packages(),
    data_files=None
)
