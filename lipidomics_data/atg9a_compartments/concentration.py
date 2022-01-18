#!/usr/bin/env python3


import numpy as np
import math
import os, sys
import pandas as pd
import argparse

def average(csv):
    
    df = pd.read_csv(csv)
    df1 = df[0:6] # select the rows for the name
    
    # drop everything besides sample 
    df = df.drop([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
    df = df.reset_index(drop=True)
    df1 = df1.T.reset_index(drop=True).T
    df = df.drop([2,3]) # keep starved samples
    df = df.T.reset_index(drop=True).T  # reset index column
    df = df.apply(pd.to_numeric, errors='coerce') # all value must be numerical
    df = df.mean().to_frame().T
    final_df = pd.concat([df1,df])
    final_df = final_df.fillna('Nan')
    final_df =final_df.drop([0,1],axis = 1)
    final_df.to_csv("final.csv")

if __name__ == '__main__':

    """
    Script to parse the csv with lipid concentration from
    lipidomics data 
    """ 

    parser = argparse.ArgumentParser()

    parser.add_argument('-i',
                        '--input',
                        dest='csv',
                        required=True,
                        metavar='',
                        help='csv',
                        )
    args = parser.parse_args()
    csv = args.csv
    average(csv)