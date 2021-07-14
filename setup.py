from setuptools import setup, find_packages

setup(

    name="Calculator",
    version="0.0.1",
    description="its a calculator",
    author="kamran raza",
    author_email="",
    url="",
    packages=find_packages(

        where = 'src',
        include = ['*',],
    ),
    package_dir = {"":"src"}

)