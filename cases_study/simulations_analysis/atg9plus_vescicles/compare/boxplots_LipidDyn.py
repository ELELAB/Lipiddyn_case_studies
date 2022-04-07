import sys
import os
import os.path as path
import argparse
import shutil
from pathlib import Path
import glob
import numpy as np
import logging
import pandas as pd 
import tempfile
import yaml
import seaborn as sns
import matplotlib.pyplot as plt
from functools import reduce
sns.set_theme()

def plot1(files):
    l_df = []
    for xvg in files:
        df = pd.read_csv(xvg,
                         skiprows=15,
                         names=["Membrane",
                                "Lower leaflet",
                                "Upper leaflet"],
                                sep="    ")
        df = df["Membrane"]
        l_df.append(df)
    i = 0
    ax = plt.subplot(111)
    for dataframe in l_df:
        
        dataframe= pd.DataFrame(dataframe)
        dataframe["position"] = i
        ax.boxplot(dataframe["Membrane"],
                   positions = [i],
                   patch_artist=True,
                   )
        i += 1
    plt.xticks([0, 1, 2], 
               ["35%DOPC24%CHOL19%PSM13%LSM9%NSM",
                 "59%DOPC19%PSM13%LSM9%NSM",
                "100%DOPC"])
    plt.savefig("boxplot_thickness.pdf",dpi=300)



if __name__ == '__main__':
    files = list(sys.argv[1:])
    plot1(files)
    

    
	
