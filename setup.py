import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OsuPyParser",
    version="0.2.0",
    author="Lenforiee",
    author_email="lenforiee@misumi.me",
    description="A powerful package for parsing .osu extention file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lenforiee/osupyparser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
