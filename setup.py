import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="KronoPI_cybergenik", # Replace with your own username
    version="0.0.1",
    author="Luciano Remes",
    author_email="cybergenik@gmail.com",
    description="Generates random 4 digit number using user time and date from PI digits",
    url="https://github.com/Cybergenik/KronoPI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)