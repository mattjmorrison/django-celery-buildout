
from setuptools import setup

setup(
    name="django-project",
    version="0.1",
    description="Django app using buildout",
    author="Matthew J. Morrison",

    package_dir={'': 'src'},
    install_requires = (
        'django==1.2.3',
        'mock',          
        'django-debug-toolbar',
		'celery',
		'django-celery',
		'ghettoq',
		
    ),
)
