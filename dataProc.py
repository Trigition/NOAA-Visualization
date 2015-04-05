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

def printRow(row):
    lat1 = row[1]['LATITUDE']
    long1 = row[1]['LONGITUDE']
    eventID = row[1]['EVENT_ID']
    episodeID = row[1]['EPISODE_ID']
    stormType = row[1]['EVENT_TYPE']
    if str(lat1) != "nan" and isInt(str(episodeID)):
        print "*"*10, "ENTRY", "*"*10
        print "Episode ID: ", episodeID
        print "Latitude: " + str(lat1).ljust(10) + " Longitude: " + str(long1).ljust(10)
        print "Storm Type: ", stormType
    
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 1000)
data = pd.read_csv('correctedData.csv')
for row in data.iterrows():
    printRow(row)
