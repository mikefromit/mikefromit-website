from setuptools import find_packages, setup

setup(
    name='ox-sprint',
    version='0.0.1',
    description='',
    long_description='',
    license='',
    author='m1yag1',
    author_email='',
    packages=find_packages(),
    install_requires=[
        'Flask==0.12.2',
        'Flask-Security==3.0.0',
        'github3.py==0.9.6',
        'redis==2.10.6'
    ],
    extras_require={
        'dev': [
            'pytest==3.1.3',
            'pytest-runner==2.11.1',
            'pytest-cov==2.5.1',
            'WebTest==2.0.23'
        ]
    },
    tests_require=[
        'pytest',
    ],
    setup_requires=[
        'pytest-runner'
    ],
    classifiers=[],
)
