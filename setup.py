
from setuptools import find_packages, setup


version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

if "-" in version:
    # when not on tag, git describe outputs: "1.3.3-22-gdf81228"
    # pip has gotten strict with version numbers
    # so change it to: "1.3.3+22.git.gdf81228"
    # See: https://peps.python.org/pep-0440/#local-version-segments
    v,i,s = version.split("-")
    version = v + "+" + i + ".git." + s

setup(
    name="sbatchpy",
    version=version,
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
