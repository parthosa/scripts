import os, shutil,re

a=os.listdir()

regex=re.compile(r'\d\d-\d\d-\d\d\d\d')

def fucked(s):
    if regex.search(s)==None:
        return False
    return True

for i in a:
    if fucked(i):
        mo=regex.search(i)

        meow=[]
        meow.append(mo.group()[3])
        meow.append(mo.group()[4])
        meow.append('-')
        meow.append(mo.group()[0])
        meow.append(mo.group()[1])

        for j in mo.group()[5:]:
            meow.append(j)

        meow2=''.join(meow)

        print (meow2)

        new=i.replace(mo.group(),meow2)







        shutil.move(i,new)
