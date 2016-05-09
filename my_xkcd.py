import requests,bs4,os
n=1600

while(n!=1590):
 url='http://xkcd.com/'+str(n)
 res=requests.get(url)
 soup=bs4.BeautifulSoup(res.text,"html.parser")

 image=soup.select('#comic img')[0].get('src')
 image='http://'+image[2:]

 res2=requests.get(image)

 f=open('image'+str(n)+'.png','wb')
 n-=1
 for i in res2.iter_content(100000000):
    f.write(i)

 f.close()
