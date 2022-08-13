from setuptools import setup, find_packages


setup(
    name="sbatchpy",
    version="0.0.2",
    packages=find_packages(exclude=["tests.*", "tests", "figs", "examples"]),
    author="Killian Sheriff",
    author_email="ksheriff@mit.edu",
    description="Python package to easily run sbatch jobs.",
    license="MIT",
    keywords=["sbatch", "slurm", "python", "hpc"],
    url="https://github.com/killiansheriff/sbatchpy",
    install_requires=[
        "",
    ],
    include_package_data=True,
)


