import os
from setuptools import setup

path = os.path.dirname(__file__)
long_desc_fd = os.path.join(path, 'README.md')

long_description = ''

with open(long_desc_fd) as f:
    long_description = f.read()

setup(
    name='jackhanma',
    version='0.0.1',
    packages=['jackhanma'],
    url='https://github.com/sillyfatcat/jackhanma',
    license='MIT',
    author='Shelby Shum',
    author_email='sshum00@gmail.com',
    description='Django implementation for golink',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['golink', 'tinyurl', 'shorthand'],
    download_url='https://github.com/sillyfatcat/jackhanma/archive/v0.1.tar.gz',
    install_requires=[
        'django',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
