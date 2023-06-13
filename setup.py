import requests
from setuptools import find_packages, setup


def get_latest_version():
    api_url = "https://api.github.com/repos/killiansheriff/sbatchpy/releases/latest"
    response = requests.get(api_url)
    if response.status_code == 200:
        release_info = response.json()
        tag_name = release_info["tag_name"]
        # Extract the version number from the tag name
        version = re.match(r"v?(\d+\.\d+\.\d+)", tag_name)
        if version:
            return version.group(1)
    return "0.0.1"  # Default version if fetching fails


setup(
    name="sbatchpy",
    version=get_latest_version(),
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
