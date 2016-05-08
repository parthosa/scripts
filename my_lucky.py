
import sys, requests, bs4,webbrowser

url='https://www.google.com/search?q='
url+='+'.join(sys.argv[1:])
res=requests.get(url)

soup=bs4.BeautifulSoup(res.text,'html.parser')

elems=soup.select('h3 a[href]')

for i in elems[:3]:

    webbrowser.open('https://www.google.com/'+i.get('href'))
