#script to cut the trajectory on the last microsecond of the simulation
source /usr/local/gromacs-2019.4/bin/GMXRC

#tot elongation = 21 microsec 

#b= 20  microsec ; e= 21 microsec
gmx_mpi make_ndx -f ../../../../../../../../../../../../../simulations/p23_p24/membrane_bound/p24_163-193/model_63/heterogeneous/pc-50_sm-20_chol-30/popc_dpsm_chol/replicate1/MARTINI/md/prot_memb/md_prot_memb.tpr -o index.ndx << eof
r 7-27
1 | 13 | 14
q
eof

#execute the command to cut the traj and fit on protein transmembrane helix
gmx_mpi trjconv -f ../../../../../../../../../../../../../simulations/p23_p24/membrane_bound/p24_163-193/model_63/heterogeneous/pc-50_sm-20_chol-30/popc_dpsm_chol/replicate1/MARTINI/md/prot_memb/center_traj_prot_memb.xtc \
              -s ../../../../../../../../../../../../../simulations/p23_p24/membrane_bound/p24_163-193/model_63/heterogeneous/pc-50_sm-20_chol-30/popc_dpsm_chol/replicate1/MARTINI/md/prot_memb/md_prot_memb.tpr \
              -o center_cut.xtc -n index.ndx \
              -b 19600000 -e 20600000 \
              -fit rotxy+transxy

#run analysis
LipidDyn -f center_cut.xtc \
		 -s ../../../../../../../../../../../../../simulations/p23_p24/membrane_bound/p24_163-193/model_63/heterogeneous/pc-50_sm-20_chol-30/popc_dpsm_chol/replicate1/MARTINI/md/prot_memb/update.gro \
		 -g ../coarse_grained.yml \
		 -p -n 8 -2d -enr

#Calculate density of the protein
gmx_mpi densmap -f center_cut.xtc \
              -s ../../../../../../../../../../../../../simulations/p23_p24/membrane_bound/p24_163-193/model_63/heterogeneous/pc-50_sm-20_chol-30/popc_dpsm_chol/replicate1/MARTINI/md/prot_memb/md_prot_memb.tpr \
              -o densmap_prot.xpm -n index.ndx -dmin 0 -dmax 8.6 << eof
1
eof

#convert densmap to eps
gmx_mpi xpm2ps -f densmap_prot.xpm -o densmap_prot.eps
