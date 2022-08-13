#!/bin/bash
#SBATCH --no-requeue
#SBATCH --mem=1gb
#SBATCH --time=00:01:00
#SBATCH --account=myaccount
#SBATCH --cpus-per-task=5
#SBATCH --partition=shared
#SBATCH --ntasks-per-node=1
#SBATCH --nodes=1
#SBATCH --job-name=myjob_2var1_Bvar2.sh
#SBATCH --output=out/myjob_2var1_Bvar2.out
source activate base 
 python my_script.py 2 B