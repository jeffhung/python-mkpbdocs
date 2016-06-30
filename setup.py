# -*- coding: utf-8

#from distutils.core import setup
from setuptools import setup

import mkpbdocs

setup(
    name='mkpbdocs',
    version=mkpbdocs.__version__,
    author=mkpbdocs.__author__,
    author_email=mkpbdocs.__email__,
    url='https://github.com/jeffhung/python-mkpbdocs',
    license="BSD",
    description='Protobuf documentation with MkDocs.',
    long_description=mkpbdocs.__doc__,
    platforms=[ 'noarch' ],
    packages=[ 'mkpbdocs' ],
    scripts=[],
    include_package_data=True,
    install_requires=[ 'protobuf >= 2.5.0' ],
    tests_require=[
        'pytest >= 2.5.1',
        'watchdog >= 0.8.3',
    ],
    entry_points={
        'console_scripts': [
            'mkpbdocs = mkpbdocs.mkpbdocs:main',
            'protoc-gen-pbdocs = mkpbdocs.pb2json:main',
        ]
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

