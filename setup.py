from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="evalogger",
    version="0.1.1",
    description="Small and simple logging library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tevtongermany/evalogger",
    author="Tevtongermany",
    author_email="Tevtongermany@femboy.cx",
    license="Apache License 2.0",
    packages=find_packages(),
    install_requires=["aiohttp", "requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
