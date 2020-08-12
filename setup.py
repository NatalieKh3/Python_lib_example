from setuptools import setup
setup(
    name="library1",
    version="0.0.1",
    description="this library is for fun",
    author="natalie",
    author_email="hvannatalya@gmail.com",
    url="https://github.com/NatalieKh3/Python_lib_example",
    license="MIT",
    packages=["library1","library2"],
    install_requires=[
        "numpy==1.19.1"
    ]
)