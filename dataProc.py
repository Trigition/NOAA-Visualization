#!/usr/bin/python2.7

from glob import glob
import pandas as pd
import re
###Notes###
#1997 Bad Formatted Line on 26199,26200,31380

#DEFINE CSV HEADERS AS INTS FOR INDEXING COLUMNS
#Year and Month Entries
Begin_YearMonth = 1
End_YearMonth = 4
#Day Entries
Begin_Day = 2
End_Day = 5
#Time Entries
Begin_Time = 3
End_Time = 6
#Storm Type
Storm_Type = 13
State = 11
Property_Damage = 25

Begin_Latitude = 45
Begin_Longitude = 46
End_Latitude = 47
End_Longitude = 48
def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def df_fromFile(filename):
    FullPath = './data/NOAA_StormData/uncompressed/' + filename
    return pd.read_csv(FullPath, low_memory=False)

def series_fromFile(filename, header_index):
    FullPath = './data/NOAA_StormData/uncompressed/' + filename
    return pd.Series.from_csv(FullPath, index_col=header_index)

def printRow(row):
    Month = row[1]['MONTH_NAME']
    Year = row[1]['YEAR']
    print "Year: ", Year, "Month: ", Month

def print_csv_columns(df):
    i = 0
    for type in df.columns.values.tolist():
        print i, type
        i += 1

pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 1000)

sortingDict = {'January': 1, 'February': 2, 'March': 3, 'April': 4,
               'May': 5, 'June': 6, 'July': 7, 'August': 8,
               'September': 9, 'October': 10, 'November': 11, 'December': 12}

<<<<<<< HEAD
data = openDataFile('concatedDataAll')
#data['MONTH_RANK'] = data['MONTH_NAME'].map(sortingDict)
data = data.sort(columns=['YEAR', 'MONTH_RANK'], ascending=True)

for row in data.iterrows():
    printRow(row)
=======
convertedData = pd.DataFrame(columns=['eventID', 'episodeID', 'begin_lat', 'begin_long',
                                      'end_lat', 'end_long', 'begin_day', 'month',
                                      'end_day', 'year', 'stormType', 'propertyDamage'])
data = df_fromFile('concatedDataAll')
#for row in data.iterrows():
    #Determine Time Parameters
    #beginDay = row[1]['BEGIN_DAY']
    #endDay = row[1]['END_DAY']
    #month = row[1]['MONTH_NAME']
    #year = row[1]['YEAR']
    #eventID = row[1]['EVENT_ID']
    #episodeID = row[1]['EPISODE_ID']
    #beginLat = row[1]['BEGIN_LAT']
    #beginLong = row[1]['BEGIN_LON']
    #endLat = row[1]['END_LAT']
    #endLong = row[1]['END_LON']
    #stormType = row[1]['EVENT_TYPE']
    #damage = row[1]['DAMAGE_PROPERTY']
    #print "On:", month, ",", year, "a", stormType, "occured."
stormTypes = series_fromFile('concatedDataAll', Storm_Type)
print stormTypes
>>>>>>> 15a26f476b3632845a168b8a5af57531664cf77d
