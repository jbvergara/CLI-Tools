import setuptools

long_description = ""
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jbvergara-cmd_tools",
    version="0.0.1",
    author="Jemuel Bryan Vergara",
    author_email="jemuel.bryan.vergara@gmail.com",
    description="A collection of command line utilities.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git-codecommit.ap-southeast-1.amazonaws.com/v1/repos/jem-cmd-tools-project",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=(
        'requests',
    ),
)