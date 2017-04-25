# -*- coding: utf-8 -*-
"""`sphinx_cobra_theme`.


"""
from setuptools import setup
from sphinx_cobra_theme import __version__


setup(
    name='sphinx_cobra_theme',
    version=__version__,
    url='https://github.com/uni-lu/sphinx_cobra_theme/',
    license='MIT',
    author='Sylvain Arreckx',
    author_email='sylvain.arreckx@gmail.com',
    description='Cobra theme for Sphinx based on ReadTheDocs theme.',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=['sphinx_cobra_theme'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
