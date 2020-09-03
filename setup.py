# coding: utf-8
__author__ = 'CotherArt'

from setuptools import setup


setup(
    name='taskmaster',
    version='0.2',
    install_requires=['Click',],
    py_modules=['taskmaster', 'listhandler', 'item'],
    entry_points='''
    [console_scripts]
    hello=taskmaster:hello
    '''
)
