from setuptools import setup


repo_url = 'https://github.com/chillaranand/httpie-django-auth'
author = 'Chillar Anand'
author_email = 'anand21nanda@gmail.com'


with open('README.rst') as fh:
    long_description = fh.read()

setup(
    name='httpie-django-auth',
    version='0.1.1',
    description='django Auth plugin for HTTPie.',
    long_description=long_description,

    author=author,
    author_email=author_email,
    maintainer=author,
    maintainer_email=author_email,

    url=repo_url,
    download_url=repo_url,

    py_modules=['httpie_django_auth'],

    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_django_auth = httpie_django_auth:DjangoAuthPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0'
    ],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
