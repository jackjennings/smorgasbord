from setuptools import setup

setup(
    name='smorgasbord',
    version='0.0.2',
    author='Jack Jennings',
    author_email='j@ckjennin.gs',
    packages=['smorgasbord'],
    url='http://github.com/jackjennings/smorgasbord',
    license='LICENSE',
    description='Reports language coverage given a set of unicode values',
    long_description=open('README.rst').read(),
    install_requires=['unicodeset'],
    include_package_data=True
)
