# nude pics downloader
# give the name of pornstar as argument, the script will create a folder
# with pornstar's name in your current working directory
# and will download 20 nude pics of her and store them in that folder

import bs4,requests,os,sys,webbrowser

pornstar=' '.join(sys.argv[1:])

os.makedirs('./'+pornstar,exist_ok=True)
os.chdir('./'+pornstar)
stuff='+'.join(sys.argv[1:])+'+nude'
url='https://www.google.com/search?q='+stuff+'&source=lnms&tbm=isch'

res=requests.get(url)
soup=bs4.BeautifulSoup(res.text,'html.parser')
elems=soup.select('div a img')

for i in range(20):
    f=open('nude_pic_'+str(i+1)+'.jpeg','wb')
    res2=requests.get(elems[i].get('src'))
    for chunk in res2.iter_content(10000000):
        f.write(chunk)
    f.close()

os.chdir('./..')
