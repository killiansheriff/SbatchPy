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
