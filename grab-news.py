from bs4 import BeautifulSoup

import requests

url = "https://www.breitbart.com"
url = "https://www.breitbart.com"

#url = raw_input("silahkan masukan website nya:")

r = requests.get(url)

data = r.text

soup = BeautifulSoup(data,"lxml")


#section = soup.find("section", {'class': 'featured_side'})
#for link in section:
#	print( link.find("h2"))

i = 0;
max = 1
section = soup.select(".post h2.title a")
for link in section:
 print(link.text.encode("utf-8"))