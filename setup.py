from setuptools import find_packages, setup


setup(
    name='mikefromit-website',
    version='0.0.1',
    description='mikefromit personal site',
    long_description='',
    license='MIT',
    author='mikefromit',
    author_email='mike.arbelaez@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Flask==0.12.2',
        'Flask-Security==3.0.0',
        'github3.py==0.9.6',
        'redis==2.10.6',
        'click==6.7',
        'Flask==0.12.2',
        'gevent==1.2.2',
        'greenlet==0.4.12',
        'gunicorn==19.7.1',
        'itsdangerous==0.24',
        'Jinja2==2.9.6',
        'MarkupSafe==1.0',
        'redis==2.10.6',
        'Werkzeug==0.12.2'
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
