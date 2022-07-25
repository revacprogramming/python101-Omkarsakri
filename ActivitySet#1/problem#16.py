# Databases
# https://www.py4e.com/lessons/database
from urllib.request import urlopen
from bs4 import BeautifulSoup


url = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
html = urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")
href = soup('a')
#print href

for i in range(count):
    link = href[position].get('href', None)
    print (href[position].contents[0])
    html = urlopen(link).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')




"""from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
req = Request("http://py4e-data.dr-chuck.net/known_by_Ceitidh.html")
html_page = urlopen(req)
soup = BeautifulSoup(html_page,"lxml") 
lnk = []
for i in soup.find_all('a'):
    lnk.append(i.get('href'))
for i in range(7):
  req = Request(lnk[17])
  html_page = urlopen(req)
  soup = BeautifulSoup(html_page,"lxml")
  for title in soup.find_all('title'):
    print(title.get_text())
  lnk.clear()
  for i in soup.find_all('a'):
    lnk.append(i.get('href')"""
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
#om
