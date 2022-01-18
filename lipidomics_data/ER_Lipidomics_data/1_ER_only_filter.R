#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)
#arg1 species.xlsx arg2 classes.xlsx
library("xlsx")

#read the sheet with the species from lipidomics 
Species_all_replicates <- read.xlsx(args[1], 1, check.names=FALSE)
Species_median <- read.xlsx(args[1], 2, check.names=FALSE)

#filter dataset based on the codes of the ER replicates from the file samples.csv
Species_all_replicates_ER <- Species_all_replicates[c("NA","35_1_040","35_1_041","35_2_040","35_2_041","35_3_040","35_3_041","35_4_040","35_4_041","35_5_040")]
#filter dataset on the ER
Species_median_ER <- Species_median[c("NA","ER")]
#rename column 
names(Species_all_replicates_ER)[1] <- ''
names(Species_median_ER)[1] <- ''

#Write the filtered ER xlsx file in the same starting format
write.xlsx(Species_all_replicates_ER, file="species_ER.xlsx", sheetName="Species_all_replicates", append=FALSE, row.names = FALSE)
write.xlsx(Species_median_ER, file="species_ER.xlsx", sheetName="Species_median", append=TRUE, row.names = FALSE)
#########################

#read the sheet with the classes from lipidomics
Classes_all <- read.xlsx(args[2], 1, check.names=FALSE)
Classes_median <- read.xlsx(args[2], 2, check.names=FALSE)
Classes_all_no_CE_Lyso_FA <- read.xlsx(args[2], 3, check.names=FALSE)
Classes_median_no_CE_Lyso_FA <- read.xlsx(args[2], 4, check.names=FALSE)

#filter dataset based on the codes of the ER replicates from the file matches.txt
Classes_all_ER <- Classes_all[c("NA","35_1_040","35_1_041","35_2_040","35_2_041","35_3_040","35_3_041","35_4_040","35_4_041","35_5_040")]
Classes_all_no_CE_Lyso_FA_ER <- Classes_all_no_CE_Lyso_FA[c("NA","35_1_040","35_1_041","35_2_040","35_2_041","35_3_040","35_3_041","35_4_040","35_4_041","35_5_040")]
#filter dataset on the ER
Classes_median_ER <- Classes_median[c("variable","ER")]
Classes_median_no_CE_Lyso_FA_ER <- Classes_median_no_CE_Lyso_FA[c("NA","ER")]
#rename column 
names(Classes_all_ER)[1] <- ''
names(Classes_all_no_CE_Lyso_FA_ER)[1] <- ''
names(Classes_median_ER)[1] <- ''
names(Classes_median_no_CE_Lyso_FA_ER)[1] <- ''
Classes_median_no_CE_Lyso_FA_ER <- na.omit(Classes_median_no_CE_Lyso_FA_ER)

#Write the filtered ER xlsx file in the same starting format
write.xlsx(Classes_all_ER, file="classes_ER.xlsx", sheetName="Classes_all", append=FALSE, row.names = FALSE)
write.xlsx(Classes_median_ER, file="classes_ER.xlsx", sheetName="Classes_median", append=TRUE, row.names = FALSE)
write.xlsx(Classes_all_no_CE_Lyso_FA_ER, file="classes_ER.xlsx", sheetName="Classes_all_no_CE_Lyso_FA", append=TRUE, row.names = FALSE)
write.xlsx(Classes_median_no_CE_Lyso_FA_ER, file="classes_ER.xlsx", sheetName="Classes_median_no_CE_Lyso_FA", append=TRUE, row.names = FALSE)
