import os


def write_line(fh, key, value):
    """Write sbatch line

    Args:
        fh (object): file object that we write on.
        key (str): sbatch option parameter.
        value (str): value corresponding to the sbatch option parameter.
    """
    fh.writelines(f"#SBATCH --{key}={value}\n")


def get_preset(key):
    """Get configuration preset.

    Args:
        key (str): preset name.

    Returns:
        dict: sbatch configuration dictionary (preset).
    """
    presets = {
        "cpu_shared": {
            "partion": "shared",
            "time": "01:00:00",
            "nodes": "1",
            "cpus-per-tasks": "5",
            "ntasks-per-node": "1",
        },
        "gpu_debug": {
            "partion": "gpu-debug",
            "gpus": "1",
            "cpus-per-tasks": "5",
            "time": "00:30:00",
            "nodes": "1",
        },
    }
    return presets[key]


def write_sbatch(options, code, load_preset="", job_directory=f"{os.getcwd()}/.job"):
    """Write and run sbatch file.

    Args:
        options (dict): dict containing sbatch keys and attributes.
        code (str): code to be run in the slurm job.
        load_preset (str, optional): name of the preset to be loaded. Defaults to "".
        job_directory (str, optional): Folder path to where sbatch jobs will be written. Defaults to f"{os.getcwd()}/.job".

    Returns:
        str: path of the sbatch file created.
    """

    if load_preset != "":
        try:
            get_preset(load_preset).update(options)
        except:
            print("preset not implemented!")

    os.makedirs(job_directory, exist_ok=True)
    job_file = os.path.join(job_directory, options["job-name"])
    with open(job_file, "w") as fh:
        fh.writelines("#!/bin/bash\n")
        fh.writelines("#SBATCH --no-requeue\n")

        for key in options:
            write_line(fh, key, options[key])
        fh.writelines(code)
    fh.close()
    return job_file


def run_sbatch(job_file):
    """Run sbatch file

    Args:
        job_file (str): path to the sbatch file to be submitted.
    """
    os.system(f"sbatch {job_file}")


def run(
    options,
    code,
    load_preset="",
    job_directory=f"{os.getcwd()}/.job",
    check_dirname=True,
    cleanup=False,
):
    """Write and run sbatch file.

    Args:
        options (dict): dict containing sbatch keys and attributes.
        code (str): code to be run in the slurm job.
        load_preset (str, optional): name of the preset to be loaded. Defaults to "".
        job_directory (str, optional): Folder path to where sbatch jobs will be written. Defaults to f"{os.getcwd()}/.job".
        cleanup: if True delete .job folder
    """
    # check that output directory exist otherwise stop
    if "output" in options:
        dirname = os.path.dirname(options["output"])

        if check_dirname:
            if not os.path.isdir(dirname) and dirname != "":
                print(f"This jobs was not submitted as {dirname} does not exist.")
                return

    job_file = write_sbatch(options, code, load_preset=load_preset, job_directory=job_directory)
    run_sbatch(job_file)

    if cleanup:
        os.rmdir(job_directory)
