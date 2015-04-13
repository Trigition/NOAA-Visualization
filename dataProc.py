#!/usr/bin/python2.7

from glob import glob
import pandas as pd
import re
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
    Month = row[1]['MONTH_NAME']
    Year = row[1]['YEAR']
    print "Year: ", Year, "Month: ", Month

def timesort(entry1, entry2):
    longDate1, shortDate1 = ()

pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 1000)

sortingDict = {'January': 1, 'February': 2, 'March': 3, 'April': 4,
               'May': 5, 'June': 6, 'July': 7, 'August': 8,
               'September': 9, 'October': 10, 'November': 11, 'December': 12}

data = openDataFile('concatedDataAll')
#data['MONTH_RANK'] = data['MONTH_NAME'].map(sortingDict)
data = data.sort(columns=['YEAR', 'MONTH_RANK'], ascending=True)

for row in data.iterrows():
    printRow(row)
