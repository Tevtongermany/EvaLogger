from setuptools import setup, find_packages

setup(
    name="evalogger",
    version="0.1.0",
    description="Small and simple logging library",
    author="Tevtongermany",
    author_email="Tevtongermany@femboy.cx",
    packages=find_packages(),
    install_requires=["aiohttp", "requests"],
)
