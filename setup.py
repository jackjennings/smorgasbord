import codecs
import os
import re

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='smorgasbord',
    version=find_version('smorgasbord', '__init__.py'),
    author='Jack Jennings',
    author_email='j@ckjennin.gs',
    packages=['smorgasbord'],
    url='http://github.com/jackjennings/smorgasbord',
    license='MIT',
    description='Reports language coverage given a set of unicode values',
    long_description=open('README.rst').read(),
    install_requires=['unicodeset'],
    include_package_data=True
)
