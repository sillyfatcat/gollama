import os
from setuptools import setup, find_packages

path = os.path.dirname(__file__)
long_desc_fd = os.path.join(path, 'README.md')

long_description = ''

with open(long_desc_fd) as f:
    long_description = f.read()

setup(
    name='gollama',
    version='1.0.2',
    packages=find_packages(),
    url='https://github.com/sillyfatcat/gollama',
    license='MIT',
    author='Shelby Shum',
    author_email='sshum00@gmail.com',
    description='Django implementation for golink',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['golink', 'tinyurl', 'shorthand'],
    download_url='https://github.com/sillyfatcat/gollama/archive/v0.1.tar.gz',
    install_requires=[
        'django',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Internet :: Name Service (DNS)',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
