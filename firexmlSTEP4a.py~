
#### Steps 1, 2, & 3 are good, 4 is sloppy
#### Step 4, how to remove these "\r\n\r\n"
#### Why only one row, how to get all rows?
#### How to export as csv file?
#### csv.writer >> http://docs.python.org/2/library/csv.html, http://docs.python.org/3/library/csv.html, http://stackoverflow.com/questions/5701962/python-csv-writer, http://www.pythonforbeginners.com/systems-programming/using-the-csv-module-in-python/, http://en.kioskea.net/faq/2091-python-read-and-write-csv-files


#STEP 1: IMPORT 
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup as Soup 
import requests
import csv


# STEP 2: PULL REQUEST
input = requests.get("http://www.toronto.ca/fire/cadinfo/livecad.xml")
#url = raw_input("www.toronto.ca/fire/cadinfo/livecad.xml")
#
data = input.text
#print data


#STEP 3: MAKE A SOUP
xml= data
soup = Soup(xml)
print soup.prettify()



#STEP 4: PARSE (SLOPPY CLEAN THIS LATER)
export = []
# NOTE 'update' is from a different place in xml file
update = soup.update_from_db_time.renderContents()
#update = updateZ.renderContents()
## make Z names
mainZ = soup.prime_street
streetsZ = soup.cross_streets
time2Z = soup.dispatch_time
numberZ = soup.event_num 
eventZ = soup.event_type
alarmZ = soup.alarm_lev
beatZ = soup.beat
unitsZ = soup.units_disp
## make names with rendered content
main = mainZ.renderContents()
streets = streetsZ.renderContents()
time2 = time2Z.renderContents()
number = numberZ.renderContents()
event = eventZ.renderContents()
alarm = alarmZ.renderContents()
beat = beatZ.renderContents()
units = unitsZ.renderContents()
# append to export
export.append([update, main, streets, time2, number, event, alarm, beat, units])

#STEP 5: PRINT
print export

#STEP 6: Write CSV

f = open(firelist, w)
wr = csv.writer(f, quoting=csv..QUOTE_ALL)
wr.writerow(export)




