#In order to run the LipidDyn analysis the input files are:
# a) trajectory file in xtc format with fixed pbc issues 
# b) reference gro file, including same atoms as the xtc file
# c) yaml configuration file (full_atom.yml)  provided in the working directory

# Run the bash script "run_lipidDyn.sh" to reproduce the analysis of APL, Thickness 
# and Order Parameter calculation on the case of study of homogeneous membrane
# for atg9a+ like vesicles 

# The input gro and xtc files are retrieved from ../../../../../../../../../simulations/atg9plus_vescicles/homogeneous/pc-100_1/dopc/replicate1/CHARMM36/md/LipidDyn

bash run_lipidDyn.sh
