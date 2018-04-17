from setuptools import setup

setup(
    name='deepmatcher',
    description='A deep learning package for entity matching',
    version='0.0.1',
    packages=['deepmatcher', 'deepmatcher.data', 'deepmatcher.models'],
    install_requires=['torch>=0.3.1', 'tqdm', 'pyprind', 'six', 'Cython', 'fastText==0.1.1'],
    dependency_links=[
        'http://github.com/facebookresearch/fastText/tarball/master#egg=fastText-0.1.1'
    ])
