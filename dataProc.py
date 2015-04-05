#!/usr/bin/python2.7

from glob import glob
import pandas as pd

###Notes###
#1997 Bad Formatted Line on 26199,26200,31380

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def openDataFile(filename):
    FullPath = './data/NOAA_StormData/uncompressed/' + filename
    return pd.read_csv(FullPath, low_memory=False)

def printRow(row):
    data = row[1]['END_DATE_TIME']
    print data

pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 1000)

data = openDataFile('concatedDataAll')
data = data.sort('YEAR', ascending=True)
for row in data.iterrows():
    printRow(row)
