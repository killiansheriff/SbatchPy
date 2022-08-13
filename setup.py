from setuptools import setup, find_packages


setup(
    name="sbatchpy",
    version="0.0.2",
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


