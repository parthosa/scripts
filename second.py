import os

f=open("first.py","r")

f2=open("new.py","w")


for i in str(f.read()):
    if i=='/':
        f2.write('#')
    else:
        f2.write(i)


f.close()
f2.close()

f3=open("first.py","w")
f4=open("new.py","r")

for i in str(f4.read()):
    f3.write(i)
f3.close()
f4.close()

os.system('python3 first.py')
os.system('rm new.py')
