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

f = open('output.txt', 'w')
f.write('')
f.close()

date = soup.find('update_from_db_time').text.strip()

count = 1
for item in soup.find_all("event"):
    
    f = open('output.txt', 'a')
    f.write('Event #' + str(count) + '\n' + '--------' + '\n')
    f.write('Date: ' + date + '\n')
    count += 1
    for tag in item:
        if (str(tag.name) == 'None'):
            continue
        f.write(str(tag.name) + ': ')
        text = tag.string.strip()
        f.write(text)
        f.write('\n')
    f.write('\n')
    f.close()
    
# print soup.find_all("event").renderContents()

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
