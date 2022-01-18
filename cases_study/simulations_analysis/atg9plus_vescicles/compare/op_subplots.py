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
import requests
import tempfile
import yaml
import seaborn as sns
import matplotlib.pyplot as plt
from functools import reduce
sns.set_theme()


def plot(files):
    fig, (ax1, ax2) = plt.subplots(1,2,figsize=(16,8))
    plot1 = []
    plot2 = []
    for csv in files:
        df = pd.read_csv(csv)
        for sn in ['sn1','sn2']:
            df1 = df[df['OP_name'].str.contains(sn)] # split in sn1 and sn2   
            sn_x = df1['atom2'].str[1:-1] # extract the x axis
            sn_y = df1['OP_mean'] # extract the y axis
            
            if sn == 'sn1':
             
                ax1.plot(sn_x,-sn_y,)
                ax1.scatter(sn_x,-sn_y,marker='_')
                ax1.set_ylim([0.0, 0.3])
            if sn == 'sn2':
               
                ax2.plot(sn_x,-sn_y,)
                ax2.scatter(sn_x,-sn_y,marker='_')
                ax2.set_ylim([0.0, 0.3])
    plt.legend(["35%DOPC24%CHOL19%PSM13%LSM9%NSM",
                "59%DOPC19%PSM13%LSM9%NSM",
                "100%DOPC"],
                loc='upper right')
    plt.savefig("OP_DOPC_combined.pdf")
if __name__ == '__main__':
    files = list(sys.argv[1:])
    plot(files)
