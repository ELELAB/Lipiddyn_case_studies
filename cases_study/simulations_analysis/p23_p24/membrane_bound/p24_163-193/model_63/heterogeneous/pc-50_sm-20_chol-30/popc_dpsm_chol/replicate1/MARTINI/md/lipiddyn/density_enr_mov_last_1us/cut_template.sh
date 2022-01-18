#script to cut the trajectory on the last microsecond
source /usr/local/gromacs-2019.4/bin/GMXRC



#tot elongation = 20.6 microsec 

#b= 19.6  microsec ; e= 20.6 microsec


#execute the command to cut the traj
gmx_mpi trjconv -f ../../../../../../../../../../../../../simulations/p23_p24/membrane_bound/p24_163-193/model_63/heterogeneous/pc-50_sm-20_chol-30/popc_dpsm_chol/replicate1/MARTINI/md/prot_memb/center_traj_prot_memb.xtc \
              -s ../../../../../../../../../../../../../simulations/p23_p24/membrane_bound/p24_163-193/model_63/heterogeneous/pc-50_sm-20_chol-30/popc_dpsm_chol/replicate1/MARTINI/md/prot_memb/md_prot_memb.tpr \
              -o center_cut.xtc -n ../../../../../../../../../../../../../simulations/p23_p24/membrane_bound/p24_163-193/model_63/heterogeneous/pc-50_sm-20_chol-30/popc_dpsm_chol/replicate1/MARTINI/md/prot_memb/index_memb.ndx -b 19600000 -e 20600000


