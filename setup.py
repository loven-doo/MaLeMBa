from setuptools import setup, find_packages

setup(
    name='MaLeMBa',
    version='0.1.0',
    author="Denis Moshensky",
    author_email="loven-doo@fbb.msu.ru",  #
    description="Machine Learning Models Base",
    url="https://github.com/loven-doo/MaLeMBa",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",  #
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    package_data={},
    install_requires=[
        'numpy >= 1.15.3',
        'pandas >= 0.23.4',
        'scipy >= 1.1.0',
    ],
    entry_points={
        'console_scripts': []
    }
)