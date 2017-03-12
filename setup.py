from setuptools import setup


setup(
    name='scrimenv',
    version='0.0.1',
    description='Windows Python CLI Shim',
    author='Dan Bradham',
    author_email='danielbradham@gmail.com',
    scripts=[
        'bin/scrimenv.bat',
        'bin/scrimenv.ps1'
    ],
    entry_points={
        'console_scripts': ['scrimenv = pyscrimenv:cli']
    },
    py_modules=['scrimenv'],
    install_requires=[
        'click>=6.7',
        'virtualenv',
        'scrim'
    ]
)
