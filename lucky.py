import requests,sys,bs4,webbrowser

a=sys.argv[1:]
b='+'.join(a)
c='http://google.com/search?q='+b

res=requests.get(c)

html_text=res.text

soup=bs4.BeautifulSoup(html_text)

linkElems=soup.select('.r a')

numOpen=min(5,len(linkElems))

for i in range(numOpen):
    webbrowser.open('http://google.com'+linkElems[i].get('href'))
    
