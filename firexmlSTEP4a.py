#### Steps 1, 2, & 3 are good, 4 is sloppy
#### Step 4, how to remove these "\r\n\r\n"
#### Why only one row, how to get all rows?
#### How to export as csv file?
#### csv.writer >> http://docs.python.org/2/library/csv.html, http://docs.python.org/3/library/csv.html, http://stackoverflow.com/questions/5701962/python-csv-writer, http://www.pythonforbeginners.com/systems-programming/using-the-csv-module-in-python/, http://en.kioskea.net/faq/2091-python-read-and-write-csv-files

#STEP 1: IMPORT 
from bs4 import BeautifulSoup as Soup 
import requests
import csv
from scraper import Scraper

url = "http://www.toronto.ca/fire/cadinfo/livecad.xml"
scraper = Scraper(url)
soup = Soup(scraper.text)
# soup = Soup(scraper.text, "xml")

print soup
# print scraper.soup.find_all("event")

#STEP 4: PARSE (SLOPPY CLEAN THIS LATER)
export = []
# NOTE 'update' is from a different place in xml file
# update = soup.update_from_db_time.renderContents()
# main = soup.prime_street.renderContents()
# streets = soup.cross_streets.renderContents()
# time2 = soup.dispatch_time.renderContents()
# number = soup.event_num.renderContents() 
# event = soup.event_type.renderContents()
# alarm = soup.alarm_lev.renderContents()
# beat = soup.beat.renderContents()
# units = soup.units_disp.renderContents()
# # 
# # append to export
# export.append([update, main, streets, time2, number, event, alarm, beat, units])
# 
# #STEP 5: PRINT
# print export
# 
# #STEP 6: Write CSV
# 
# f = open(firelist, w)
# # wr = csv.writer(f, quoting=csv..QUOTE_ALL)
# # wr.writerow(export)
