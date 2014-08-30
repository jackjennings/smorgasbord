from setuptools import setup
from smorgasbord import __version__

setup(
    name='smorgasbord',
    version=__version__,
    author='Jack Jennings',
    author_email='j@ckjennin.gs',
    packages=['smorgasbord'],
    url='http://github.com/jackjennings/smorgasbord',
    license='LICENSE',
    description='Reports language coverage given a set of unicode values',
    long_description=open('README.rst').read(),
    install_requires=[]
)
