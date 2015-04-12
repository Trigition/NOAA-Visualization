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

pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 1000)

sortingDict = {'January': 1, 'February': 2, 'March': 3, 'April': 4,
               'May': 5, 'June': 6, 'July': 7, 'August': 8,
               'September': 9, 'October': 10, 'November': 11, 'December': 12}

convertedData = pd.DataFrame(columns=['eventID', 'episodeID', 'begin_lat', 'begin_long',
                                      'end_lat', 'end_long', 'begin_day', 'month',
                                      'end_day', 'year', 'stormType', 'propertyDamage'])
data = openDataFile('concatedDataAll')
#data['MONTH_RANK'] = data['MONTH_NAME'].map(sortingDict)
#data = data.sort(columns=['YEAR'], ascending=True)
print data.columns.values.tolist()
for row in data.iterrows():
    #Determine Time Parameters
    beginDay = row[1]['BEGIN_DAY']
    endDay = row[1]['END_DAY']
    month = row[1]['MONTH_NAME']
    year = row[1]['YEAR']
    eventID = row[1]['EVENT_ID']
    episodeID = row[1]['EPISODE_ID']
    beginLat = row[1]['BEGIN_LAT']
    beginLong = row[1]['BEGIN_LON']
    endLat = row[1]['END_LAT']
    endLong = row[1]['END_LON']
    stormType = row[1]['EVENT_TYPE']
    damage = row[1]['DAMAGE_PROPERTY']
    print "On:", month, ",", year, "a", stormType, "occured."