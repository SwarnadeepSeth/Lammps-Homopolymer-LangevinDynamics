## Homopolymer simulation using Lammps in Bulk

#### * The coarse-graining of the polymer follows the Grest-Kremer bead-spring model.
#### * The EV interaction between any two monomers along the chain is given by a short-range Lennard-Jones (LJ) potential.
#### * The connectivity between two neighboring monomers is modeled as the FENE spring potential.
#### * A three-body bending potential is used to model the chain's persistence length.

--------------------------------------------------------------------------------------------------------------------------------------------------- </br>
a) chain3d.py code generates the initial configuration of a linear homopolymer chain of the size of "PartcleN".</br>
b) Poly3d.lam code is written in Lammps that simulates the polymer trajectories using Langevin dynamics.   
c) Simulated trajectories are written in both lammpstrj and dcd format. A simulation movie can be constructed using VMD software by using the lammpstrj file. To analyze the trajectories and to extract the equilibrium statistical properties the dcd file is used in the config_analysis.py file.
