import pandas as pd
import os
import sys
import argparse
import numpy as np
#pd.set_option('display.max_columns', 1000)




def convert_xlsx(xlsx,
                 sheet,
                 out):

    # Read lipidomics dataset sheet
    df = pd.read_excel(xlsx,
                       sheet, 
                       index_col=None)
    df1 = df[0:18]
    df2 = df[18::]
    df2 = df2._convert(numeric=True)
    df2 = df2.round(3)
    df_final = pd.concat([df1, df2], ignore_index=True)
    df_final = df_final[:-2]
    mean = df_final.loc[18:19,:].tail(2).mean(axis=0).round(3).to_frame().T
    mean.insert(0,"COD.EXT", "Average Starved", True)
    df3 = pd.concat([df_final, mean], ignore_index=True)
    df3.to_csv(out, encoding='utf-8', index=False,na_rep='NULL')
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i',
                        '--input',
                        dest='xlsx',
                        type=str,
                        required=True,
                        help='name xslx file')
    parser.add_argument('-s',
                        '--sheet',
                        dest='sheet',
                        type=str,
                        required=True,
                        help='name of the sheet to load with pandas')
    parser.add_argument('-o',
                        '--ouput',
                        dest='out',
                        type=str,
                        required=True,
                        help='output name')
 
    
    args = parser.parse_args()
    xlsx = os.path.abspath(args.xlsx)
    sheet_name = args.sheet
    out_name = args.out
    convert_xlsx(xlsx,
                 sheet_name,
                 out_name)

