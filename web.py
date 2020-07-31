https://github.com/makkoncept/yts.am_scraper_/blob/master/yify_browse.py

import requests
from bs4 import BeautifulSoup as soup
res=requests.get('https://yts.mx/')
#print(res.text)
s = soup(res.text, 'lxml')
e = s.select('.browse-movie-link')
r =s.select('.rating')
print(e)
print(r)
for i in range(len(e)):
    print(e[i].figure.img["src"],end=" ")
    print(r[i].text)



'''from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as Ureq
#rl = 'https://www.flipkart.com/search?q=redmi&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
rl1='https://yts.mx/'
uClient = Ureq(rl1)
page_html = uClient.read()
uClient.close()
page_soup = Soup(page_html, "html.parser")
contain = page_soup.findAll("div", {"class":"browse-movie-link"})

#print(Soup.prettify(con[0]))
print(contain)
print(len(contain))
'''
'''
container = con[0]
#print(container.div.img["alt"])

price=container.findAll("div", {"class":"niH0FQ"})
#print(price[0].text)

rate=container.findAll("div", {"class":"_1vC4OE _2rQ-NK"})
#print(rate[0].text)

for i in range(len(con)):
    container = con[i]
    print(container.div.img["alt"])
    price = container.findAll("div", {"class": "niH0FQ"})
    print(price[0].text)
    rate = container.findAll("div", {"class": "_1vC4OE _2rQ-NK"})
    print(rate[0].text)
'''
