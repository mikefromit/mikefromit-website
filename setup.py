from pip.req import parse_requirements
from setuptools import find_packages, setup

install_requirements = parse_requirements('requirements.txt')

setup(
    name='mikefromit-website',
    version='0.0.1',
    description='mikefromit personal site',
    long_description='',
    license='MIT',
    author='mikefromit',
    author_email='mike.arbelaez@gmail.com',
    packages=find_packages(),
    install_requires=install_requirements(),
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
