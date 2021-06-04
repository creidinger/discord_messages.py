from setuptools import setup
# source: https://packaging.python.org/tutorials/packaging-projects/
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="discord_messages.py",
    version="0.0.0",
    author="Chase Reidinger",
    author_email="chase.reidinger@adepdev.com",
    description="A python interface for the Discord API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["discord_messages"],
    url="https://github.com/creidinger/discord_messages.py",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
