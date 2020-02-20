#!/bin/sh
# This file is named infinite_medium.sh
#SBATCH --partition=pre
#SBATCH --time=1-00:00:00
#SBATCH --ntasks=40
#SBATCH --cpus-per-task=4

mpirun -np $SLURM_NTASKS python2.7 cont_soil.py --db_path=$DATABASE_PATH --sim_name="cont_soil" --num_particles=1e6 --threads=$SLURM_CPUS_PER_TASK
