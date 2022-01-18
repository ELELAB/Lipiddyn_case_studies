#### Script to parse the lipidomics dataset on endoplasmic reticulum of Hela cells from Maeda's group.

The script membrane_composition.py parses the lipidomics dataset and allows the design of the composition of a membrane bilayer of any size, in terms of the total number of lipids, resembling the concentration of several classes of lipids from lipidomics data.

We used the python3 membrane_composition.py to parse the file classes.xlsx, retrieve the lipidomics data of classes of lipids of the endoplasmatic reticulum membranes, and design the composition of the membrane for the CG simulations of an endoplasmatic reticulum-like bilayer using MARTINI force field. The concept behind the script is to design membrane bilayers that resemble the concentration of the different classes of lipids from lipidomics. Furthermore, to take into account the diversity in each class of lipid we included till the four most abundant lipid species for the most abundant classes in the endoplasmatic reticulum (i.e. PC, PE, PI, PS, SM) while till the two most abundant lipid species for the less abundant classes in the endoplasmatic reticulum.

#### Raw data file:
classes_ER.xlsx - automatically parsed by the script
species_ER.xlsx - used to retrieve the lipid species and their concentrations to be given in input to the script

#### Requirements to use the script membrane_composition.py
-python3
-pandas python library
-openpyxl python library
-matches.txt dictionary file containing the association with the name of the lipid species in the raw data from lipidomics and the name of the corresponding lipid species in the MARTINI force field
-activate python3.7 environment . /usr/local/envs/py37/bin/activate 

#### Run the script

python3 membrane_composition.py classes_ER.xlsx

The steps of the scripts are:
1. parses the file classes.xlsx in the sheet Classes_median_no_CE_Lyso_FA in which it has been calculated by lipidomics the concentration of 19 class of lipids for ER from their median measured in all the experimental samples, not including the classes of lipids called Lyso, CE, FA, that are intermediates or have a role as energy storage. The concentration of each class of lipid is reported as a percentage over the total number of lipids minus the classes of lipids excluded.
2. asks in input the data of which membranes use for the calculations. We here selected the endoplasmatic reticulum entering "0". The script shows the concentration of each class of lipid.
3. simplifies the 19 classes of lipids (Cer, CerP, Chol, CL, DAG, diHexCer, GM2, GM3, HexCer, PA, PC , PCO-, PE, PEO-, PG, PI, PS, SM, triHexCer) in 13 classes by merging the similar ones (Cer=Cer+CerP+diHexCer+triHexCer, Chol, CL, DAG, GM2, GM3, PA, PC=PC+PCO-, PE=PE+PEO-, PG, PI, PS, SM).
4. asks in input the number of lipids composing each leaflet of the final membrane bilayer to design (i.e. choosing 1000 means that the final membrane bilayer should be composed of 2000 lipids in total). We here selected 1000 lipids for the bilayer system.
5. asks in input the number of lipid species to include for the first class of lipid (Cer) and then to input the name of each lipid species selected and its concentration. The lipid species names and their concentrations are taken from the species.xlsx file from the Species_median tab which includes the median of the values of lipid species concentrations calculated over all the experimental replicas for each organelle membrane. We here selected to include till the four most abundant lipid species for the most abundant classes in the endoplasmatic reticulum (i.e. PC, PE, PI, PS, SM) while till the two most abundant lipid species for the less abundant classes in the endoplasmatic reticulum.
In details we included:

Insert the number of lipid species and concentrations for Cer: 2
Enter spec: Cer 42:2;2
Enter concentration: 0.062694381
Enter spec: Cer 34:1;2
Enter concentration: 0.055038404
Inserting pair  ['Cer 42:2;2', 0.062694381]  in  Cer
Inserting pair  ['Cer 34:1;2', 0.055038404]  in  Cer

Insert the number of lipid species and concentrations for Chol: 1
Enter spec: Chol
Enter concentration: 6.17130048
Inserting pair  ['Chol', 6.17130048]  in  Chol

Insert the number of lipid species and concentrations for CL: 1
Enter spec: CL 70:5
Enter concentration: 0.016834509
Inserting pair  ['CL 70:5', 0.016834509]  in  CL

Insert the number of lipid species and concentrations for DAG: 2
Enter spec: DAG 34:1
Enter concentration: 1.105064968
Enter spec: DAG 32:1   
Enter concentration: 0.506848109
Inserting pair  ['DAG 34:1', 1.105064968]  in  DAG
Inserting pair  ['DAG 32:1', 0.506848109]  in  DAG

Insert the number of lipid species and concentrations for GM2: 0
No lipid spec-conc pair for  GM2

Insert the number of lipid species and concentrations for GM3: 1
Enter spec: GM3 34:1;2
Enter concentration: 0.018256456
Inserting pair  ['GM3 34:1;2', 0.018256456]  in  GM3

Insert the number of lipid species and concentrations for PA: 1
Enter spec: PA 34:2
Enter concentration: 0.039594096
Inserting pair  ['PA 34:2', 0.039594096]  in  PA

Insert the number of lipid species and concentrations for PC: 4
Enter spec: PC 34:1
Enter concentration: 16.9774432
Enter spec: PC 32:1
Enter concentration: 11.95001518
Enter spec: PC 36:2
Enter concentration: 7.658187
Enter spec: PC 34:2
Enter concentration: 7.249121815
Inserting pair  ['PC 34:1', 16.9774432]  in  PC
Inserting pair  ['PC 32:1', 11.95001518]  in  PC
Inserting pair  ['PC 36:2', 7.658187]  in  PC
Inserting pair  ['PC 34:2', 7.249121815]  in  PC

Insert the number of lipid species and concentrations for PE: 3
Enter spec: PE 36:2    
Enter concentration: 0.744555426
Enter spec: PE 34:2
Enter concentration: 0.408128
Enter spec: PE 38:5
Enter concentration: 0.420319577
Inserting pair  ['PE 36:2', 0.744555426]  in  PE
Inserting pair  ['PE 34:2', 0.408128]  in  PE
Inserting pair  ['PE 38:5', 0.420319577]  in  PE

Insert the number of lipid species and concentrations for PG: 1
Enter spec: PG 36:1
Enter concentration: 0.050791584
Inserting pair  ['PG 36:1', 0.050791584]  in  PG

Insert the number of lipid species and concentrations for PI: 3
Enter spec: PI 38:4
Enter concentration: 1.092488726
Enter spec: PI 36:2
Enter concentration: 0.73962885
Enter spec: PI 34:1
Enter concentration: 0.705447199
Inserting pair  ['PI 38:4', 1.092488726]  in  PI
Inserting pair  ['PI 36:2', 0.73962885]  in  PI
Inserting pair  ['PI 34:1', 0.705447199]  in  PI

Insert the number of lipid species and concentrations for PS: 1
Enter spec: PS 36:1
Enter concentration: 0.08142809
Inserting pair  ['PS 36:1', 0.08142809]  in  PS

Insert the number of lipid species and concentrations for SM: 2
Enter spec: SM 34:1;2
Enter concentration: 0.34801975
Enter spec: SM 42:2;2
Enter concentration: 0.19030476
Inserting pair  ['SM 34:1;2', 0.34801975]  in  SM
Inserting pair  ['SM 42:2;2', 0.19030476]  in  SM

6. calculates the final number of lipids of each lipid class and species in the membrane leaflet. In details, the script:
i) sums the concentrations of the lipid species for each class
ii) calculates the difference between the sum of the concentrations of the lipid species and the concentration of the corresponding lipid class
iii) divides this difference for the number of lipid species and uses the obtained value to equally increase the concentration of each lipid species
iv) uses the corrected concentration of each lipid species to calculate the final whole number of lipid in the defined membrane leaflets. In the case of a lipid number with decimals, the script returns the rounded number as the nearest integer.
v) sums of the calculated number of lipids. If the sum is not equal to the select total number of lipids the script corrects the difference by increasing or decreasing the less abundant species of the most abundant class. In our case for the endoplasmatic reticulum, the total num of lipids was 997 so we include 3 additional lipids of the species PC 34:2 in the class PC.
7. prints the output in the file out.txt. 

The out.txt contains: i) the name of each lipid class in the raw data, ii) the name of the selected lipid species in the raw data, iii) their corresponding names in the MARTINI force field, iv) the number of lipids for each species and class to design the membrane leaflets. The number of lipids and their names can be used in CHARMM-GUI to generate the membrane bilayer.
