#to run the LipidDyn analysis the input files are:
#-trajectory file in xtc format with fixed pbc issues 
#-reference gro file, including same atoms as the xtc file
#-yaml configuration file (coarse_grained.yml)  provided in the working directory

#cd density_enr_mov_last_1us/

-Run the bash script lipiddyn_dmaps_enr.sh to reproduce the analysis of 2Dmaps and Enrichment calculation on the last 1us of the simulation: the traj file center_cut.xtc is stored in the current directory 


For the p24 163-193 model we generated  100  models with Modeller (mod10.1) stored in 

/data/raw_data/computational_data/modeller_data/p23_p24/free/p24_model_probuilder_163-193/models_100/

and we  selected the best model according to a ranking score that can be retrieved in 

/data/user/shared_projects/LipidDyn_pipeline/cases_study/modeller_analysis/p23_p24/free/p24_model_probuilder_163-193/models_100/selected_model/ 

N.B. The analysis included here are the ones revised and tested so far 10th December 2021

The input gro and xtc files are retrieved from ../../../../../../../../../../../../simulations/p23_p24/membrane_bound/p24_163-193/model_63/heterogeneous/pc-50_sm-20_chol-30/popc_dpsm_chol/replicate1/MARTINI/md/prot_memb
along with the information about the system setup of the simulation
