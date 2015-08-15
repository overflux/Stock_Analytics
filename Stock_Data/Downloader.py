# print "Hello world, this is where we will download amazing incredible things."

import csv
import urllib

def formURL(stockTicker):
    filename = ''
    startMonth = '0'
    startDay = '01'
    startYear = '2005'
    endMonth = '08'
    endDay = '14'
    endYear = '2015'
    freq = 'd'

    baseURL = "http://ichart.finance.yahoo.com/" + filename + "table.csv?s="  + str(stockTicker) + "&a=" + startMonth + "&b=" + startDay + "&c=" + startYear + "&d=" + endMonth + "&e=" + endDay + "&f=" + endYear + "&g=" + freq + "&ignore=.csv"
    
    print baseURL
    return baseURL

def downloadFile(stockTicker, URL):
    try:
        print "Currently retrieving ticker: " + stockTicker
        urllib.urlretrieve(URL, "Raw_Data/" + str(stockTicker) + ".csv")
    except urllib.ContentTooShortError as e:
        outfile = open(str(stockTicker) + ".csv", "w")
        outfile.write(e.content)
        outfile.close()

f = open('Stock_Symbols.csv', 'rb')

reader = csv.reader(f)

stockSymbols = []

for row in reader:
    print row
    stockTicker = row[0]
    stockSymbols.append(row[0])
    
    URL = formURL(stockTicker)
    
    downloadFile(stockTicker, URL)
    
print "I'm done!"