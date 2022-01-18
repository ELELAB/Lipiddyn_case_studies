#### Script to parse the lipidomics dataset on ATG9A positive vescicles of starved cells from Sharon Tooze's group.

#### Raw data file:
converted.csv

#### Run the script

The script will parse the csv data and automatically run the average between concentration of only the starved cells
in this case.

To run the script:

python3 concentration.py -i  converted.csv



You will have in output a "final.csv" that can be opened with an editor as Excel.
You will also have the associated names on top of the averaged concentration.
