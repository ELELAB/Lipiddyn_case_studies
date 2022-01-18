LipidDyn -t center_cut.xtc \
		 -f ../../../../../../../../../../../../simulations/p23_p24/membrane_bound/p24_163-193/model_63/heterogeneous/pc-50_sm-20_chol-30/popc_dpsm_chol/replicate1/MARTINI/md/prot_memb/update.gro \
		 -g ../coarse_grained.yml \
		 -dmaps -enr \
		 -ncore 8 \
		 -prot

# on the last 1 us traj also available at /data/user/alessia/Lipid_plots_fig/lipiddyn_P24_MOD63_50_20_30/density_enr_last_us/center_cut.xtc
