#we here filtered the lipidomics data of Hela cells from Maeda's group to keep only the data relative to endoplasmic reticulum (species.xlsx and classes.xlsx)
#we used the R script 1_ER_only_filter.R
#it requires the R package xlsx https://github.com/colearendt/xlsx
# run it as 

Rscript 1_ER_only_filter.R ../species.xlsx ../classes.xlsx
