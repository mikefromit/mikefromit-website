from setuptools import find_packages, setup


setup(
    name='mikefromit-website',
    version='0.0.1',
    description='mikefromit personal site',
    long_description='',
    license='MIT',
    author='mikefromit',
    author_email='mike@mikefromit.com',
    packages=find_packages(),
    install_requires=[
        "alembic==0.9.6",
        "Babel==2.5.1",
        "beautifulsoup4==4.6.0",
        "blinker==1.4",
        "certifi==2017.7.27.1",
        "chardet==3.0.4",
        "click==6.7",
        "coverage==4.4.1",
        "Flask==0.12.2",
        "Flask-BabelEx==0.9.3",
        "Flask-Login==0.4.0",
        "Flask-Mail==0.9.1",
        "Flask-Principal==0.4.0",
        "Flask-Security==3.0.0",
        "Flask-SQLAlchemy==2.3.2",
        "Flask-WTF==0.14.2",
        "gevent==1.2.2",
        "github3.py==0.9.6",
        "greenlet==0.4.12",
        "gunicorn==19.7.1",
        "idna==2.6",
        "itsdangerous==0.24",
        "Jinja2==2.9.6",
        "Mako==1.0.7",
        "MarkupSafe==1.0",
        "mikefromit-website==0.0.1",
        "passlib==1.7.1",
        "py==1.4.34",
        "pytest==3.1.3",
        "python-dateutil==2.6.1",
        "python-editor==1.0.3",
        "pytz==2017.3",
        "redis==2.10.6",
        "requests==2.18.4",
        "six==1.11.0",
        "speaklater==1.3",
        "SQLAlchemy==1.1.15",
        "uritemplate==3.0.0",
        "uritemplate.py==3.0.2",
        "urllib3==1.22",
        "waitress==1.1.0",
        "WebOb==1.7.3",
        "Werkzeug==0.12.2",
        "WTForms==2.1",
    ],
    extras_require={
        'dev': [
            'coverage==4.4.1'
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
