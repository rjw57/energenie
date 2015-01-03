import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="energenie",
    version="1.0.1",
    author="Ben Nuttall",
    author_email="ben@raspberrypi.org",
    description="Remotely control power sockets from the Raspberry Pi",
    license="BSD",
    keywords=[
        "energenie",
        "raspberrypi",
    ],
    url="https://github.com/bennuttall/energenie",
    packages=[
        "energenie",
    ],
    install_requires=[
        "RPi.GPIO",
    ],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Home Automation",
        "License :: OSI Approved :: BSD License",
    ],
)
