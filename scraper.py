from BeautifulSoup import BeautifulStoneSoup as Soup
import requests
import csv

class Scraper:

  def __init__(self, url):
    self.url = url

  def get(self):
    return requests.get(self.url)

  def response(self):
    return self.get()

  @property
  def text(self):
    return self.response().text

  def show(self):
    print self.text
    return False
