import setuptools

def read_me_file():
    with open("README.md", "r") as fh:
        long_description = fh.read()
    return long_description

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=read_me_file(),
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    install_requires=_requires_from_file('requirements.txt'),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)