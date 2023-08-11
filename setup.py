import os

from setuptools import find_packages, setup

# Get description from README
root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, "README.md"), "r", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="sbatchpy",
    version="1.0.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests.*", "tests", "figs", "examples"]),
    author="Killian Sheriff",
    author_email="ksheriff@mit.edu",
    description="Sbatchpy is a python package allowing easy sbatch job script creation and submissions on hpc clusters, directly from python.",
    license="MIT",
    keywords=["sbatch", "slurm", "python", "hpc"],
    url="https://github.com/killiansheriff/sbatchpy",
    install_requires=[
        "",
    ],
    include_package_data=True,
)
