import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "energenie",
    version = "0.1.1",
    author = "Ben Nuttall",
    author_email = "ben@raspberrypi.org",
    description = "Python module to control the Energenie add-on board for the Raspberry Pi used for remotely turning power sockets on and off.",
    license = "BSD",
    keywords = [
        "energenie",
        "raspberrypi",
    ],
    url = "https://github.com/bennuttall/energenie",
    packages = [
        "energenie",
    ],
    long_description = read('README.md'),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Topic :: Home Automation",
        "License :: OSI Approved :: BSD License",
    ],
)
