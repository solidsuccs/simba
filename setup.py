import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="simba",
    version="2020.08.11.06",
    description="Manage output from scientific simulations",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/solidsuccs/simba",
    author="Brandon Runnels",
    author_email="brunnels@uccs.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["simba"],
    include_package_data=True,
    #install_requires=["feedparser", "html2text"],
    entry_points={
        "console_scripts": [
            "simba=simba.__main__:main",
        ]
    },
)