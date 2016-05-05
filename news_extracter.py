''' This script will extract headlines from
3 news websites and print them on the screen'''


import requests,bs4

# getting relevant data from google news
a=requests.get('https://news.google.com/')
soup1=bs4.BeautifulSoup(a.text,"html.parser")
elems1=soup1.select('.titletext')

# getting relevant data from hackernews
b=requests.get('https://news.ycombinator.com/')
soup2=bs4.BeautifulSoup(b.text,"html.parser")
elems2=soup2.select('td[class="title"] a[href]')

# getting relevant data from bing news
c=requests.get('http://www.bing.com/news/search?q=&nvaug=%5bNewsVertical+Category%3d%22rt_World%22%5d&FORM=NWBTCB')
soup3=bs4.BeautifulSoup(c.text,"html.parser")
elems3=soup3.select('div[class="newstitle"] a[href]')

###########################
print('headlines from google news:')
print()
for i in range(5):
    print(str(i+1)+'  '+elems1[i].getText())
print()
print()
##############################
print('headlines from hackernews:')
print()

#print the headlines
for i in range(5):
    print(str(i+1)+'  '+elems2[i].getText())

print()
print()
##############################
print('headlines from bing news:')
print()

#print the headlines
for i in range(5):
    print(str(i+1)+'  '+elems3[i].getText())

print()
print()    
