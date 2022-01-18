#The folder contains a bash script used to perform the ranking of p24 models obtained with modeller and stored in the folder:
/data/user/shared_projects/modeller_data/p23_p24/free/p24_model_probuilder_163-193/models_100/models

# the ranking  is computed with the python script
selection_model_analysis.py

# the best model is selected according to the highest ranking score and based on two different criteria:
#1. the distance between the CA of the C-term and N-term residues and the number of contacts with a cutoff of 4 A between
#2. the number of contacts with a cutoff of 4 A, between: i) each atom of the residues composing the C-term disordered region and of the helix domain
# ii) each atom of the residues composing the N-term disordered region and of the helix domain 
# iii) each atom of each residue composing the C-term and N-term (inner contacts). 
#the final rank is given by averaging the  min-max normalized  N/C-term distances (norm_dist) and the reverse min-max normalized the numeber contacts (norm_c)--> norm_c+norm_d/2

#Here we assess the model quality of 100 p24_163-193 structures where p24_169-189 structurefrom probuilder has been used as template 

#In the bash script model_selection.sh, the user should provide the path of the folder in which all the model structures are stored and the residue 
#positions to consider to compute the contact, specifying the last and first residues at the C-term and N-term of the disordered regions and the last and first position of the helix region 
#In the case of the p24 structure we will consider the following positions:

nf=163  #first position of the n-term disordered region
nl=168  #last position of the n-term disordered region 
cf=190  #first position of the c-term disordered region 
cl=193  #last position of the c-term disordered region 
helix_f=169 #first position of the helix region 
helix_l=189 #last postion of the helix region 

#The bash script creates a folder called /ranking and here execute the python script which returns the .tsv files: distance.tsv; contact.tsv; merged.tsv. 
#The bash script also creates a new folder in model_100/ called selected_model/
#From the merged.tsv the user can select the first models (highest ranks) and move it on the folder /selected_model. 

