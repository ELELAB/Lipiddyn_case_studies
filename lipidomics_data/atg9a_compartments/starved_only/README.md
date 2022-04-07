# Setup of membrane systems starting from lipidomics data

We here filtered the lipidomics data of ATG9A-positive compartments of HEK293 cells from Tooze's lab to keep only the data relative to starved cells (Kopi_af_14_0020_Sharon_Tooze.xlsx).
The script will compute the average relative abundance for each lipid in the dataset. These are used to setup the membrane models using CHARMM-GUI as explained below.

<br/>

## Run the script

"python3.7 convert_xlsx.py -i Kopi_af_14_0020.xlsx -s "Raw data" -o data_final.csv"

<br/>

## Reading the output 

The output file contains the informations in a dataframe organized in the following manner:
<br/>

        VARIABLE OWL ID          CLASS     SUBCLASS A            SUBCLASS C              INDIVIDUAL NOTATION  ... SIMPLIFIED NAME SIMPLE NAME       HMDB    KEGG average
            Cho_01            Sterols  Cholesterol and derivatives    Nan                      Cholesterol  ...             Cho         Cho  HMDB00067  C00187   0.024
            SphLip_10  Sphingolipids  Sphingomyelin  Sphingoid base d18:1                   SM(d18:1/16:0)  ...              SM          SM  HMDB10169  C00550   0.019
            SphLip_12  Sphingolipids  Sphingomyelin  Sphingoid base d18:1                   SM(d18:1/17:0)  ...              SM          SM        Nan     Nan   0.019
            SphLip_13  Sphingolipids  Sphingomyelin  Sphingoid base d18:1                   SM(d18:1/18:0)  ...              SM          SM  HMDB01348  C00550   0.015
            SphLip_30  Sphingolipids  Sphingomyelin                   Nan                         SM(42:1)  ...              SM          SM        Nan     Nan   0.013
            ...
            ...


**N.B**

From this dataframe we have selected the sphingolipids using two criteria: 
  1. the highest average relative abundance per sphingolipid 
  2. whether the topology was present or not in the CHARMM-GUI lipid library for modelling 

Ultimately we selected  the 3 following sphingolipids, the colesterol and their relative abundances: 
<br/>

    INDIVIDUAL NOTATION CHARMM	     average
    SM(d18:1/16:0)            PSM     0.019
    SM42:1                    LSM     0.013
    SM42:2                    NSM     0.009
    Cholesterol               CHL     0.024

<br/>

These final relative abundances were directly used as percentages to use as ratio in CHARMM-GUI for the setup of final systems :

    Lipid(CHARMM)  Average  CHARMM-GUI ratio(upper/lower leaflet)
    PSM	        0.019    19%
    LSM	        0.013    13%
    NSM	        0.009     9%
    CHL         0.024    24%
    -------------------------------
    Total sphingo ratio =    41% (without cholesterol)
    
<br/>

We filled the rest of the membrane with DOPC ( PC(18:1/18:1) ) as representative of the  

## Final Systems

We ended up with the following membrane systems that are the ones in our study:

1. 59% DOPC ; 19% PSM ; 13% LSM ; 9% NSM
2. 35% DOPC ; CHL 24% ; 19% PSM ; 13% LSM ; 9% NSM

In addition we modelled as a reference system a 100% DOPC system.
