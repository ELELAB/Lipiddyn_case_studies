#we here filtered the lipidomics data of ATG9A-positive compartments of HEK293 cells from Tooze's lab to keep only the data relative to starved cells (Kopi_af_14_0020_Sharon_Tooze.xlsx)
#we used the python script 1_convert_xlsx.py 
# run it as 

python 1_convert_xlsx.py -i ../Kopi_af_14_0020_Sharon_Tooze.xlsx -s "Raw data" -o converted.csv
