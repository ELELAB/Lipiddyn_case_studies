#!/bin/bash
python=python3.7 # required python version: python3.7
# set up of the arguments for the python script model_selection_analysis.py
mkdir scripts
mkdir ranking
cd scripts
cp ../model_selection_analysis.py .
rm ../model_selection_analysis.py .
cd ..

cd ranking
cp ../scripts/model_selection_analysis.py .
# path in which models are stored
path=../../../../../../modeller/p23_p24/free/p24_model_probuilder_163-193/models_100/models/
# set the position ranges
cf=190
cl=193
nf=163
nl=168
helix_f=169
helix_l=189

#execute the python  script
$python model_selection_analysis.py -p $path -C $cf $cl -N $nf $nl -H $helix_f $helix_l

cd ..
mkdir selected_model


