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

def csvFromSeries(filename, series):
    FullPath = './data/NOAA_StormData/uncompressed/' + filename
    series.to_csv(FullPath)

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
input_file = 'concatedDataAll'
raw_data = df_fromFile(input_file)
#print_csv_columns(raw_data)
usable_data = raw_data[['BEGIN_LAT', 'BEGIN_LON',
                        'END_LAT', 'END_LON',
                        'BEGIN_YEARMONTH', 'BEGIN_DAY', 'BEGIN_TIME',
                        'END_YEARMONTH', 'END_DAY', 'END_TIME']]
usable_data.sort(['BEGIN_YEARMONTH', 'BEGIN_DAY', 'BEGIN_TIME'], ascending=True, inplace=True)
usable_data.reset_index
print usable_data
usable_data.to_csv('./ProjectPage/' + 'data.csv')
