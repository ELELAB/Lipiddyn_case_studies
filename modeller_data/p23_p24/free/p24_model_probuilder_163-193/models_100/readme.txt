#As template we here used the model from Probuilder of the transmembrane helix of p24
#see repository /data/user/shared_projects/modeller_data/p23_p24/free/p24_model_probuilder_163-193/models_100/models/ for further info

#We can copy the .pdb file of the template to use in the modelling
cp /data/user/shared_projects/simulations_data/p23_p24/membrane_bound/p24_169-189/model_probuilder/heterogeneous/pc-70_chol-30/popc_chol/replicate1/MARTINI/charmm-gui-2573695789/p24_last_A.pdb .

#We here included p24 residues 169-189 from the probuilder model p24_last_A.pdb as template
#We used a longer peptide as sequence target from residues 165-193 including two additional Lys (KK) at the beggining of the sequence (163-164) 
#We used MODELLER to reconstruct the the region 163-193 keeping frozen the region in between (169-189) (no optimization by MODELLER during the modeling)
#We converted the template structure to  generate the alignment file (called xxx.ali) 
#We modified the alignment file (xxx.ali) to include the regions discussed above, specifying in the template first field 'structureM'
#We modified the MODELLER run script named modeller-multiple3.py to include the correct chain name 'A', the renumbering residue starting position and the selection of the atoms/residues that shouldn’t or should be optimized during the modeling
#We used Mod9.15 to predict the 100 models with the command 

mod9.15 modeller-multiple3.py

#we included all the models in the folder models

mkdir models
cd models

#we moved in the models folder the final models and removed the partial files created by MODELLER

mv *B9999* models
rm *V999*
rm *D000*
#We can sort the list of pdb files inside the models/ folder with the command
ls -d -- *.B99990* | sort -t. -k2
#We performed the selection of models in the modeller_analysis folder
/data/user/shared_projects/LipidDyn_pipeline/cases_study/modeller_analysis/p23_p24/free/p24_model_probuilder_163-193/models_100/

