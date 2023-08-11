# sbatchpy
![PyPI Version](https://img.shields.io/pypi/v/sbatchpy.svg) ![PyPI Downloads](https://static.pepy.tech/badge/sbatchpy) 

A python package that allows easy ``sbatch`` job script creation and submissions on ``hpc clusters``, directly from ``python``. 

# Installation

```bash
# to install latest PyPI release
pip install sbatchpy

# to install latest GitHub commit
pip install --upgrade git+https://github.com/killiansheriff/sbatchpy
```

# Usage
An example on how to run a python script called ``my_script.py`` taking 2 arguments ``var1`` and ``var2`` as inputs, and using the ``base`` environement is provided below. A complete example with outputs can be found [here](examples/).

```python
from sbatchpy.run import run

config = {
    "mem": "1gb",
    "time": "00:01:00",
    "account": "myaccount",
    "cpus-per-task": "5",
    "partition": "shared",
    "ntasks-per-node": "1",
    "nodes": "1",
}

for var1, var2 in zip([1, 2, 3], ["A", "B", "C"]):

    config["job-name"] = f"myjob_{var1}var1_{var2}var2.sh"
    config["output"] = f"out/myjob_{var1}var1_{var2}var2.out"
    run(
        config,
        code=f"source activate base \n python my_script.py {var1} {var2}",
    )

```
By default, sbatchpy will check that ``config["output"]``'s directory folder exists. If it doesn't, you will be notified and the job will not run. 

Additionally, each sbatch submission script is saved inside the ``f"{os.getcwd()}/.job"`` folder. Another saving folder can be chosen by passing ``job_directory=my_saving_directory_path`` to the ``run`` function which is responsible of creating the submission script and running it using ``sbatch job_directory/config["job-name"]``.



