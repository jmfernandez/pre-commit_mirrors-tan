from setuptools import setup

import os.path
tan_version = "0.0.0"
with open(os.path.join(os.path.dirname(__file__), ".version")) as vH:
    for line in vH:
        tan_version = line.strip()
        break
setup(
    name='pre_commit_placeholder_package',
    version='0.0.0',
    install_requires=[f'tan=={tan_version}'],
)
