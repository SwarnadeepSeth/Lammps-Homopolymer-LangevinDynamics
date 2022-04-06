#!/bin/bash

#SBATCH --nodes=6
#SBATCH --ntasks-per-node=1
#SBATCH --time=240:00:00

echo "Slurm nodes assigned :$SLURM_JOB_NODELIST"

#========================================================================================#
# Load Modules
#module load lammps/lammps-31Mar17-openmpi-2.0.1-ic-2017.1.043 #(no angle shift potential)
module load lammps/lammps-30Apr2019-mvapich2-2.3.1-ic-2019.1.144
#module load lammps/lammps-3Mar20-mvapich2-2.3.1-ic-2019.3.199 #(error in avx instruction)

#========================================================================================#
# Run Codes
mpirun -np 6 lammps -in poly3d.lam

#Activate conda my_env
conda init bash
source ~/.bashrc
conda activate my_env


python3 avg_data.py
python3 dcd_analysis.py
