# setup.py

from setuptools import setup, find_packages

setup(
    name='quickreadme',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'quickreadme': ['templates/*.md'],
    },
    install_requires=[
        'click',
        'Jinja2',
    ],
    entry_points='''
        [console_scripts]
        quickreadme=quickreadme.cli:main
    ''',
    author='Luis Abrantes',
    author_email='luis.hsa@gmail.com',
    description='An open-source tool to quickly generate README.md files',
    url='https://github.com/LuisAbrantes/quickreadme',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)