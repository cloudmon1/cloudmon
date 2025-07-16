import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="cloudmon",
    version="0.1",
    author="cloudmon1",
    author_email="itsue.aasu@gmail.com",
    description="This is a test package.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
